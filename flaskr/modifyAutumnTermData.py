from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db
from pathlib import Path
import os.path
import json

bp = Blueprint('modifyAutumnTermData', __name__)

@bp.route('/CSMCC16', methods=('GET', 'POST'))
def CloudComputing():
    if request.method == "POST":
        userreq = request.form
        roomCapacity = userreq.get("capacity")
        lectureDuration = [int(userreq.get("duration"))]
        lectureFrequency = int(userreq.get("frequency"))
        newDuration = [item for item in lectureDuration for i in range(lectureFrequency)]
        a_file = open("flaskr/input_data/mainfile.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        for key in json_object.keys():
            if key == 'Modules':
                for n in range(len(json_object[key])):
                    if json_object[key][n][0] == 'CSMCC16':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        autumndata = json.load(b)
    return render_template('modifyInputData/modifyautumntermdata/CSMCC16.html', autumndata=autumndata)

@bp.route('/CSMDM16', methods=('GET', 'POST'))
def DataAnalyticsandMining():
    if request.method == "POST":
        userreq = request.form
        roomCapacity = userreq.get("capacity")
        lectureDuration = [int(userreq.get("duration"))]
        lectureFrequency = int(userreq.get("frequency"))
        newDuration = [item for item in lectureDuration for i in range(lectureFrequency)]
        a_file = open("flaskr/input_data/mainfile.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        for key in json_object.keys():
            if key == 'Modules':
                for n in range(len(json_object[key])):
                    if json_object[key][n][0] == 'CSMDM16':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        autumndata = json.load(b)
    return render_template('modifyInputData/modifyautumntermdata/CSMDM16.html', autumndata=autumndata)

@bp.route('/CSMMA16', methods=('GET', 'POST'))
def MathematicsandStatistics():
    if request.method == "POST":
        userreq = request.form
        roomCapacity = userreq.get("capacity")
        lectureDuration = [int(userreq.get("duration"))]
        lectureFrequency = int(userreq.get("frequency"))
        newDuration = [item for item in lectureDuration for i in range(lectureFrequency)]
        a_file = open("flaskr/input_data/mainfile.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        for key in json_object.keys():
            if key == 'Modules':
                for n in range(len(json_object[key])):
                    if json_object[key][n][0] == 'CSMMA16':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        autumndata = json.load(b)
    return render_template('modifyInputData/modifyautumntermdata/CSMMA16.html', autumndata=autumndata)

@bp.route('/CS3PP19', methods=('GET', 'POST'))
def ProgramminginPythonforDataScience():
    if request.method == "POST":
        userreq = request.form
        roomCapacity = userreq.get("capacity")
        lectureDuration = [int(userreq.get("duration"))]
        lectureFrequency = int(userreq.get("frequency"))
        newDuration = [item for item in lectureDuration for i in range(lectureFrequency)]
        a_file = open("flaskr/input_data/mainfile.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        for key in json_object.keys():
            if key == 'Modules':
                for n in range(len(json_object[key])):
                    if json_object[key][n][0] == 'CS3PP19':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        autumndata = json.load(b)
    return render_template('modifyInputData/modifyautumntermdata/CS3PP19.html', autumndata=autumndata)

@bp.route('/CSMRS16', methods=('GET', 'POST'))
def ResearchStudies():
    if request.method == "POST":
        userreq = request.form
        roomCapacity = userreq.get("capacity")
        lectureDuration = [int(userreq.get("duration"))]
        lectureFrequency = int(userreq.get("frequency"))
        newDuration = [item for item in lectureDuration for i in range(lectureFrequency)]
        a_file = open("flaskr/input_data/mainfile.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        for key in json_object.keys():
            if key == 'Modules':
                for n in range(len(json_object[key])):
                    if json_object[key][n][0] == 'CSMRS16':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        autumndata = json.load(b)
    return render_template('modifyInputData/modifyautumntermdata/CSMRS16.html', autumndata=autumndata)

@bp.route('/INMR95', methods=('GET', 'POST'))
def BusinessDataAnalytics():
    if request.method == "POST":
        userreq = request.form
        roomCapacity = userreq.get("capacity")
        lectureDuration = [int(userreq.get("duration"))]
        lectureFrequency = int(userreq.get("frequency"))
        newDuration = [item for item in lectureDuration for i in range(lectureFrequency)]
        a_file = open("flaskr/input_data/mainfile.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        for key in json_object.keys():
            if key == 'Modules':
                for n in range(len(json_object[key])):
                    if json_object[key][n][0] == 'INMR95':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        autumndata = json.load(b)
    return render_template('modifyInputData/modifyautumntermdata/INMR95.html', autumndata=autumndata)

@bp.route('/INMR66', methods=('GET', 'POST'))
def BusinessDomainandRequirementsAnalysis():
    if request.method == "POST":
        userreq = request.form
        roomCapacity = userreq.get("capacity")
        lectureDuration = [int(userreq.get("duration"))]
        lectureFrequency = int(userreq.get("frequency"))
        newDuration = [item for item in lectureDuration for i in range(lectureFrequency)]
        a_file = open("flaskr/input_data/mainfile.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        for key in json_object.keys():
            if key == 'Modules':
                for n in range(len(json_object[key])):
                    if json_object[key][n][0] == 'INMR66':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        autumndata = json.load(b)
    return render_template('modifyInputData/modifyautumntermdata/INMR66.html', autumndata=autumndata)

@bp.route('/INMR91', methods=('GET', 'POST'))
def BusinessInformatics():
    if request.method == "POST":
        userreq = request.form
        roomCapacity = userreq.get("capacity")
        lectureDuration = [int(userreq.get("duration"))]
        lectureFrequency = int(userreq.get("frequency"))
        newDuration = [item for item in lectureDuration for i in range(lectureFrequency)]
        a_file = open("flaskr/input_data/mainfile.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        for key in json_object.keys():
            if key == 'Modules':
                for n in range(len(json_object[key])):
                    if json_object[key][n][0] == 'INMR91':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        autumndata = json.load(b)
    return render_template('modifyInputData/modifyautumntermdata/INMR91.html', autumndata=autumndata)

@bp.route('/INMR94', methods=('GET', 'POST'))
def DigitalLeadership():
    if request.method == "POST":
        userreq = request.form
        roomCapacity = userreq.get("capacity")
        lectureDuration = [int(userreq.get("duration"))]
        lectureFrequency = int(userreq.get("frequency"))
        newDuration = [item for item in lectureDuration for i in range(lectureFrequency)]
        a_file = open("flaskr/input_data/mainfile.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        for key in json_object.keys():
            if key == 'Modules':
                for n in range(len(json_object[key])):
                    if json_object[key][n][0] == 'INMR94':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        autumndata = json.load(b)
    return render_template('modifyInputData/modifyautumntermdata/INMR94.html', autumndata=autumndata)

@bp.route('/MA2VC', methods=('GET', 'POST'))
def VectorCalculus():
    if request.method == "POST":
        userreq = request.form
        roomCapacity = userreq.get("capacity")
        lectureDuration = [int(userreq.get("duration"))]
        lectureFrequency = int(userreq.get("frequency"))
        newDuration = [item for item in lectureDuration for i in range(lectureFrequency)]
        a_file = open("flaskr/input_data/mainfile.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        for key in json_object.keys():
            if key == 'Modules':
                for n in range(len(json_object[key])):
                    if json_object[key][n][0] == 'MA2VC':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        autumndata = json.load(b)
    return render_template('modifyInputData/modifyautumntermdata/MA2VC.html', autumndata=autumndata)

@bp.route('/MA2PSM', methods=('GET', 'POST'))
def ProfessionalSkillsforMathematicians():
    if request.method == "POST":
        userreq = request.form
        roomCapacity = userreq.get("capacity")
        lectureDuration = [int(userreq.get("duration"))]
        lectureFrequency = int(userreq.get("frequency"))
        newDuration = [item for item in lectureDuration for i in range(lectureFrequency)]
        a_file = open("flaskr/input_data/mainfile.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        for key in json_object.keys():
            if key == 'Modules':
                for n in range(len(json_object[key])):
                    if json_object[key][n][0] == 'MA2PSM':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        autumndata = json.load(b)
    return render_template('modifyInputData/modifyautumntermdata/MA2PSM.html', autumndata=autumndata)

@bp.route('/CS3DP19', methods=('GET', 'POST'))
def DistributedSystemsandParallelComputing():
    if request.method == "POST":
        userreq = request.form
        roomCapacity = userreq.get("capacity")
        lectureDuration = [int(userreq.get("duration"))]
        lectureFrequency = int(userreq.get("frequency"))
        newDuration = [item for item in lectureDuration for i in range(lectureFrequency)]
        a_file = open("flaskr/input_data/mainfile.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        for key in json_object.keys():
            if key == 'Modules':
                for n in range(len(json_object[key])):
                    if json_object[key][n][0] == 'CS3DP19':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        autumndata = json.load(b)
    return render_template('modifyInputData/modifyautumntermdata/CS3DP19.html', autumndata=autumndata)

@bp.route('/MIS16', methods=('GET', 'POST'))
def SocialScience():
    if request.method == "POST":
        userreq = request.form
        roomCapacity = userreq.get("capacity")
        lectureDuration = [int(userreq.get("duration"))]
        lectureFrequency = int(userreq.get("frequency"))
        newDuration = [item for item in lectureDuration for i in range(lectureFrequency)]
        a_file = open("flaskr/input_data/mainfile.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        for key in json_object.keys():
            if key == 'Modules':
                for n in range(len(json_object[key])):
                    if json_object[key][n][0] == 'MIS16':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        autumndata = json.load(b)
    return render_template('modifyInputData/modifyautumntermdata/MIS16.html', autumndata=autumndata)

