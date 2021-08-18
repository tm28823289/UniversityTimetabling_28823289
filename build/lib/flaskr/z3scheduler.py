from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db
from pathlib import Path
import os.path
import json
from z3 import *

bp = Blueprint('z3scheduler', __name__)

@bp.route('/run-z3solver', methods=('GET', 'POST'))
def runz3Solver():
    if request.method == "GET":
        # reading and parsing JSON inputdata into python dictionary
        with open('flaskr/input_data/mainfile.json') as f:
            uniTimetable_data = json.load(f) 
        # new dictionary addition for mapping weekdays 
        days_dict = {
            0: "MONDAY",
            1: "TUESDAY",
            2: "WEDNESDAY",
            3: "THURSDAY",
            4: "FRIDAY"
        }

        # unpacking dictionary values into python list variables for ease of further processing  
        University_TimeSlot = uniTimetable_data['University time']
        Lecture_Rooms = uniTimetable_data['Lecturerooms']
        Lectures = uniTimetable_data['Modules']
        LectureTime_nonPref = uniTimetable_data['Lecture_time not prefered']
        LectureRooms_nonPref = uniTimetable_data['Lecture rooms not prefered by teaching faculty']

        Modules = []  #list for storing module names
        Duration = [] #list for storing lecture duration
        Rooms = []    #list for storing lecture room names
        Term = []     #list for storing module term

        for i in Lectures:
            Modules.append(i[0])
            Duration.append(i[2])
            Term.append(i[6])
        for i in Lecture_Rooms:
            Rooms.append(i[0])
        rooms_dict = {k : v for k, v in enumerate(Rooms)}

        event_names = ['event-%s' % (i+1) for i in range(len(Modules))]
        event_dict = dict(zip(Modules, event_names))

        for m in range(len(Lecture_Rooms)):
            for i,j in rooms_dict.items():
                    if j == Lecture_Rooms[m][0]:
                        Lecture_Rooms[m][0] = i            

        class UniClass:
            def __init__(self,module,lecture_freq,batch,capacity,faculty,event, modulename, moduleterm):
                self.module = module
                self.day = Int(f'{module}_{lecture_freq}_day')   
                self.room = Int(f'{module}_{lecture_freq}_room') 
                self.startTime = Int(f'{module}_{lecture_freq}_start_Time')
                self.endTime = Int(f'{module}_{lecture_freq}_end_Time')
                self.batch = batch
                self.capacity = capacity
                self.faculty = faculty
                self.event = event
                self.modulename = modulename
                self.moduleterm = moduleterm

        ## Instantiating the UniClass by creating an object   
        uniObj = [[UniClass(Modules[j],i,Lectures[j][4],Lectures[j][1],Lectures[j][3],event_dict[Modules[j]],Lectures[j][5], Lectures[j][6]) for i in range(len(Duration[j]))] for j in range(len(Duration))]

        ## Storing the objects of UniClass in a single list instead of 2 dimensional list.
        uniObj_sl = []
        for i in range(len(Duration)):
            for j in range(len(Duration[i])):
                uniObj_sl.append(uniObj[i][j])

        ## Constraint01: Where the module lectures could be scheduled in any of the week days
        constraint01 = []
        for i in range(len(Duration)):
            for j in range(len(Duration[i])):
                expression01 = [uniObj[i][j].day == day for day in days_dict]   
                constraint01.append(Or(*expression01))

        ## Constraint02: Wherein a particular module's lecture can't be scheduled twice in a day
        assertion02 = []
        for i in range(len(Duration)):
            expression02 = Distinct([uniObj[i][j].day for j in range(len(Duration[i]))])
            assertion02.append(expression02)
        constraint02 = [And(*assertion02)]

        ## Constraint03: Where a particular lecture time should be within the University Timeslots
        # Defining user function to convert given time from hour,minute format to minutes

        def timeToMinutes(Unitime):                 
            hour = math.floor(Unitime)
            minutes = int((Unitime - hour)*100)
            return int(hour*60 + minutes)

        # calling the user-defined function
        for i in range(len(University_TimeSlot)):
            for j in range(len(University_TimeSlot[i])):  
                University_TimeSlot[i][j] = timeToMinutes(University_TimeSlot[i][j])

        # creating Constraint03
        constraint03 = []
        for i in range(len(Duration)):
            for j in range(len(Duration[i])):
                expression03 = [And(Or(And(uniObj[i][j].endTime % 60 == 0, uniObj[i][j].endTime <= University_TimeSlot[1][1], uniObj[i][j].startTime % 60 == 0, uniObj[i][j].startTime >= University_TimeSlot[1][0]),
                        And(uniObj[i][j].startTime % 60 == 0, uniObj[i][j].startTime >= University_TimeSlot[0][0], uniObj[i][j].endTime % 60 == 0, uniObj[i][j].endTime <= University_TimeSlot[0][1])),uniObj[i][j].startTime < uniObj[i][j].endTime)]
                constraint03.append(*expression03)

        ## Constraint04: Which ensures the condition that EndTime-StartTime == Lecture_Duration
        constraint04 = []
        for i in range(len(Duration)):
            for j in range(len(Duration[i])):
                expression04 = (uniObj[i][j].endTime - uniObj[i][j].startTime) == Duration[i][j]
                constraint04.append(expression04)

        ## Constraint05: Which ensures that lecture rooms are the ones provided in JSON (modified)
        lectureRoomCapacity = {}                                
        for i in range(len(Lecture_Rooms)):
            if Lecture_Rooms[i][1] not in lectureRoomCapacity:
                lectureRoomCapacity[Lecture_Rooms[i][1]] = [Lecture_Rooms[i][0]]   # aggregating lecture rooms based on it's capacity 
            else:
                lectureRoomCapacity[Lecture_Rooms[i][1]] += [Lecture_Rooms[i][0]]  # aggregating lecture rooms based on it's capacity
                
        constraint05 = []
        for i in range(len(Duration)):
            for j in range(len(Duration[i])):
                expression05 = Or(*[uniObj[i][j].room == r for r in lectureRoomCapacity[Lectures[i][1]]])
                constraint05.append(expression05)

        ## Constraint06: Creating sixth constraint which ensures following conditions 
        # If the lectures of two separate modules are running on same day
        # AND the two modules are taken by the same facutly
        # OR the two modules are taught by the same batch 
        # OR the two modules are conducted in the same classroom
        # THEN the two module lectures should be scheduled at different timings


        constraint06 = []
        for i in range(len(uniObj_sl)):
            for j in range(len(uniObj_sl)):
                sameBatchCheck = False
                if i != j:
                    for m in range(len(uniObj_sl[i].batch)):
                        for n in range(len(uniObj_sl[j].batch)):
                            if uniObj_sl[i].batch[m] == uniObj_sl[j].batch[n]:
                                sameBatchCheck = True
                                break
                
                if uniObj_sl[i] != uniObj_sl[j]:
                    sameObjectCheck = True
                else:
                    sameObjectCheck = False
                
                if uniObj_sl[i].module != uniObj_sl[j].module:
                    sameModuleCheck = True
                else:
                    sameModuleCheck = False
                    
                if uniObj_sl[i].faculty == uniObj_sl[j].faculty:
                    sameFacultyCheck = True
                else:
                    sameFacultyCheck = False
                
                sameDayCheck = uniObj_sl[i].day == uniObj_sl[j].day
                sameRoomCheck = uniObj_sl[i].room == uniObj_sl[j].room
                moduleX_ST = uniObj_sl[i].startTime
                moduleX_ET = uniObj_sl[i].endTime
                moduleY_ST = uniObj_sl[j].startTime
                moduleY_ET = uniObj_sl[j].endTime
                        
                expression06 = If(Or(And(sameObjectCheck, sameModuleCheck, sameDayCheck, sameBatchCheck),
                            And(sameObjectCheck, sameModuleCheck, sameDayCheck, sameFacultyCheck),
                            And(sameObjectCheck, sameModuleCheck, sameDayCheck, sameRoomCheck)),
                        Or(moduleX_ST >= moduleY_ET, moduleY_ST >= moduleX_ET),          
                        True)
                constraint06.append(expression06)

        ## Constraint07: which takes into consideration the faculty's lecture time preference constraints.
        constraint07 = []
        for i in range(len(uniObj_sl)):
            for j in range(len(LectureTime_nonPref)):
                expression07 = If(uniObj_sl[i].faculty == LectureTime_nonPref[j][0],
                        And(Or(uniObj_sl[i].startTime < timeToMinutes(LectureTime_nonPref[j][1][0]),uniObj_sl[i].startTime > timeToMinutes(LectureTime_nonPref[j][1][1])),
                            Or(uniObj_sl[i].endTime < timeToMinutes(LectureTime_nonPref[j][1][0]),uniObj_sl[i].endTime > timeToMinutes(LectureTime_nonPref[j][1][1]))),
                        True)
                constraint07.append(expression07)

        ## Constraint08: which takes into consideration the faculty's lecture-room preference constraints.

        for m in range(len(LectureRooms_nonPref)):
            for n in range(len(LectureRooms_nonPref[m][1])):
                for i,j in rooms_dict.items():
                    if j == LectureRooms_nonPref[m][1][n]:
                        LectureRooms_nonPref[m][1][n] = i 
                        
        constraint08 = []
        for i in range(len(uniObj_sl)):
            for j in range(len(LectureRooms_nonPref)):
                expression08 = If(uniObj_sl[i].faculty == LectureRooms_nonPref[j][0],
                        And(*[uniObj_sl[i].room != room for room in LectureRooms_nonPref[j][1]]),
                        True)
                constraint08.append(expression08)

        ## Asserting constraints into the Z3 solver
        S = Solver()
        S.add(constraint01)
        S.add(constraint02)
        S.add(constraint03)
        S.add(constraint04)
        S.add(constraint05)
        S.add(constraint06)
        S.add(constraint07)
        S.add(constraint08)

        if S.check() == sat:
            print ("A timetable with given constraints is SATISFIABLE")
        else:
            print ("Timetable is not SATISFIABLE")

        m = S.model()

        ## A user defined function to convert back total minutes to hours:minute format

        def minutesToHours(modeltime):
            hours = modeltime // 60             # Get hours with floor division
            minutes = modeltime % 60            # Get additional minutes with modulus
            time_string = f'{hours}:{minutes}'  # Create time as a string
            return time_string 

        print_UniTimetable = {}
        mappingOfRoom = {}  ## Dictionary which maps the room variable to names of the room available in JSON file
        mappingOfDay = {}   ## Dictionary which maps the day variable to available weekdays.


        ## loop to create the 'mappingOfRoom' dictionary
        for i in range(len(uniObj_sl)):
            tempRoom = m.evaluate(uniObj_sl[i].room)
            for room in Lecture_Rooms:
                if tempRoom == room[0]:
                    mappingOfRoom[tempRoom] = room[0]

        ## Loop to create the 'mappingOfDay' dictionary
        for i in range(len(uniObj_sl)):
            tempDay = m.evaluate(uniObj_sl[i].day)
            for day in days_dict:
                if tempDay == day:
                    mappingOfDay[tempDay] = day


        ## loop to create the 'UniTimetable' dictionary
        for i in range(len(uniObj_sl)):
            if mappingOfDay[m.evaluate(uniObj_sl[i].day)] not in print_UniTimetable:
                print_UniTimetable[mappingOfDay[m.evaluate(uniObj_sl[i].day)]] = [[uniObj_sl[i].module,minutesToHours(m.evaluate(uniObj_sl[i].startTime).as_long()),minutesToHours(m.evaluate(uniObj_sl[i].endTime).as_long()),mappingOfRoom[m.evaluate(uniObj_sl[i].room)],uniObj_sl[i].faculty,uniObj_sl[i].batch, uniObj_sl[i].event, uniObj_sl[i].modulename, uniObj_sl[i].moduleterm]]
            else:
                print_UniTimetable[mappingOfDay[m.evaluate(uniObj_sl[i].day)]] += [[uniObj_sl[i].module,minutesToHours(m.evaluate(uniObj_sl[i].startTime).as_long()),minutesToHours(m.evaluate(uniObj_sl[i].endTime).as_long()),mappingOfRoom[m.evaluate(uniObj_sl[i].room)],uniObj_sl[i].faculty,uniObj_sl[i].batch, uniObj_sl[i].event, uniObj_sl[i].modulename, uniObj_sl[i].moduleterm]]

        final_dict ={}
        for k,v in days_dict.items():
            for i,j in print_UniTimetable.items():
                if i == k:
                    final_dict.update({v:j})
                    
        for m,n in rooms_dict.items():
            for o in final_dict.keys():
                for p in range(len(final_dict[o])):
                    if m == final_dict[o][p][3]:
                        final_dict[o][p][3] = n

        PG_CS_dict = {}
        PG_IMDB_dict = {}
        BSc_CS_Y1_dict = {}
        BSc_CS_Y2_dict = {}
        BSc_CS_Y3_dict = {}

        for k, v in final_dict.items():
            for p in range(len(final_dict[k])):
                for n in range(len(final_dict[k][p][5])):
                    if final_dict[k][p][5][n] == 'BSc-CS-Y1':
                        if k not in BSc_CS_Y1_dict:
                            BSc_CS_Y1_dict[k] = [final_dict[k][p]]
                        else:
                            BSc_CS_Y1_dict[k] += [final_dict[k][p]]
                    elif final_dict[k][p][5][n] == 'BSc-CS-Y2':
                        if k not in BSc_CS_Y2_dict:
                            BSc_CS_Y2_dict[k] = [final_dict[k][p]]
                        else:
                            BSc_CS_Y2_dict[k] += [final_dict[k][p]]
                    elif final_dict[k][p][5][n] == 'BSc-CS-Y3':
                        if k not in BSc_CS_Y3_dict:
                            BSc_CS_Y3_dict[k] = [final_dict[k][p]]
                        else:
                            BSc_CS_Y3_dict[k] += [final_dict[k][p]]
                    elif final_dict[k][p][5][n] == 'PG-CS':
                        if k not in PG_CS_dict:
                            PG_CS_dict[k] = [final_dict[k][p]]
                        else:
                            PG_CS_dict[k] += [final_dict[k][p]]
                    else: 
                        if k not in PG_IMDB_dict:
                            PG_IMDB_dict[k] = [final_dict[k][p]]
                        else:
                            PG_IMDB_dict[k] += [final_dict[k][p]]

        jsonString1 = json.dumps(final_dict, indent=4)
        jsonString2 = json.dumps(PG_CS_dict, indent=4)
        jsonString3 = json.dumps(PG_IMDB_dict, indent=4)
        jsonString4 = json.dumps(BSc_CS_Y1_dict, indent=4)
        jsonString5 = json.dumps(BSc_CS_Y2_dict, indent=4)
        jsonString6 = json.dumps(BSc_CS_Y3_dict, indent=4)

        jsonFile = open("flaskr/output_data/final_data.json", "w")
        jsonFile.write(jsonString1)
        jsonFile.close()

        jsonFile = open("flaskr/output_data/PG_CS.json", "w")
        jsonFile.write(jsonString2)
        jsonFile.close()

        jsonFile = open("flaskr/output_data/PG_IMDB.json", "w")
        jsonFile.write(jsonString3)
        jsonFile.close()

        jsonFile = open("flaskr/output_data/BSc_CS_Y1.json", "w")
        jsonFile.write(jsonString4)
        jsonFile.close()

        jsonFile = open("flaskr/output_data/BSc_CS_Y2.json", "w")
        jsonFile.write(jsonString5)
        jsonFile.close()

        jsonFile = open("flaskr/output_data/BSc_CS_Y3.json", "w")
        jsonFile.write(jsonString6)
        jsonFile.close()
    return render_template('viewData/timetableSchedule.html', data_dict=final_dict)
    