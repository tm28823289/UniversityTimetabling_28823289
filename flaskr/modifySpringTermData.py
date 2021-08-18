from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db
from pathlib import Path
import os.path
import json

bp = Blueprint('modifySpringTermData', __name__)

@bp.route('/CS3AI18-CSMAI19', methods=('GET', 'POST'))
def ArtificialIntelligence():
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
                    if json_object[key][n][0] == 'CS3AI18-CSMAI19':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/CS3AI18-CSMAI19.html', springdata=springdata)

@bp.route('/MMM077', methods=('GET', 'POST'))
def DigitalMarketing():
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
                    if json_object[key][n][0] == 'MMM077':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/MMM077.html', springdata=springdata)

@bp.route('/CSMBD16', methods=('GET', 'POST'))
def BigDataAnalytics():
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
                    if json_object[key][n][0] == 'CSMBD16':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/CSMBD16.html', springdata=springdata)

@bp.route('/CSMML16', methods=('GET', 'POST'))
def MachineLearning():
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
                    if json_object[key][n][0] == 'CSMML16':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/CSMML16.html', springdata=springdata)

@bp.route('/CS3VI18', methods=('GET', 'POST'))
def VisualIntelligence():
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
                    if json_object[key][n][0] == 'CS3VI18':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/CS3VI18.html', springdata=springdata)

@bp.route('/CS3VR16', methods=('GET', 'POST'))
def VirtualReality():
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
                    if json_object[key][n][0] == 'CS3VR16':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/CS3VR16.html', springdata=springdata)

@bp.route('/CSMIA19', methods=('GET', 'POST'))
def ImageAnalysis():
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
                    if json_object[key][n][0] == 'CSMIA19':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/CSMIA19.html', springdata=springdata)

@bp.route('/INMR93', methods=('GET', 'POST'))
def DigitalInnovation():
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
                    if json_object[key][n][0] == 'INMR93':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/INMR93.html', springdata=springdata)

@bp.route('/INMR89', methods=('GET', 'POST'))
def BigDatainBusiness():
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
                    if json_object[key][n][0] == 'INMR89':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/INMR89.html', springdata=springdata)

@bp.route('/INMR77', methods=('GET', 'POST'))
def BusinessIntelligenceandDataMining():
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
                    if json_object[key][n][0] == 'INMR77':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/INMR77.html', springdata=springdata)

@bp.route('/INMR86', methods=('GET', 'POST'))
def BusinessTechnologyConsulting():
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
                    if json_object[key][n][0] == 'INMR86':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/INMR86.html', springdata=springdata)

@bp.route('/INMR96', methods=('GET', 'POST'))
def DigitalHealthandDataAnalytics():
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
                    if json_object[key][n][0] == 'INMR96':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/INMR96.html', springdata=springdata)

@bp.route('/INMR65', methods=('GET', 'POST'))
def ITProjectManagement():
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
                    if json_object[key][n][0] == 'INMR65':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/INMR65.html', springdata=springdata)

@bp.route('/MA1LA', methods=('GET', 'POST'))
def LinearAlgebra():
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
                    if json_object[key][n][0] == 'MA1LA':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/MA1LA.html', springdata=springdata)

@bp.route('/MA1FM', methods=('GET', 'POST'))
def FoundationsofMathematics():
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
                    if json_object[key][n][0] == 'MA1FM':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/MA1FM.html', springdata=springdata)

@bp.route('/MA1CA', methods=('GET', 'POST'))
def Calculus():
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
                    if json_object[key][n][0] == 'MA1CA':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/MA1CA.html', springdata=springdata)

@bp.route('/CS1FC16', methods=('GET', 'POST'))
def FundamentalsofComputerScience():
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
                    if json_object[key][n][0] == 'CS1FC16':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/CS1FC16.html', springdata=springdata)

@bp.route('/ST1PS', methods=('GET', 'POST'))
def ProbabilityandStatistics():
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
                    if json_object[key][n][0] == 'ST1PS':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/ST1PS.html', springdata=springdata)

@bp.route('/MA2RCA', methods=('GET', 'POST'))
def RealandComplexAnalysis():
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
                    if json_object[key][n][0] == 'MA2RCA':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/MA2RCA.html', springdata=springdata)

@bp.route('/MA2MPR', methods=('GET', 'POST'))
def MathematicalProgramming():
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
                    if json_object[key][n][0] == 'MA2MPR':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/MA2MPR.html', springdata=springdata)

@bp.route('/MA2NAN', methods=('GET', 'POST'))
def NumericalAnalysis():
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
                    if json_object[key][n][0] == 'MA2NAN':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/MA2NAN.html', springdata=springdata)

@bp.route('/MA2DE', methods=('GET', 'POST'))
def DifferentialEquations():
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
                    if json_object[key][n][0] == 'MA2DE':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/MA2DE.html', springdata=springdata)

@bp.route('/CS2JA16', methods=('GET', 'POST'))
def Java():
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
                    if json_object[key][n][0] == 'CS2JA16':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/CS2JA16.html', springdata=springdata)

@bp.route('/CS2AO17', methods=('GET', 'POST'))
def AlgorithmsandOperatingSystems():
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
                    if json_object[key][n][0] == 'CS2AO17':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/CS2AO17.html', springdata=springdata)

@bp.route('/MA3NAT', methods=('GET', 'POST'))
def NumericalAnalysisII():
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
                    if json_object[key][n][0] == 'MA3NAT':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/MA3NAT.html', springdata=springdata)

@bp.route('/CS3DS19', methods=('GET', 'POST'))
def DataScienceAlgorithmsandTools():
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
                    if json_object[key][n][0] == 'CS3DS19':
                        json_object[key][n][1] = roomCapacity
                        json_object[key][n][2] = newDuration
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    with open("flaskr/input_data/mainfile.json", "r") as b:
        springdata = json.load(b)
    return render_template('modifyInputData/modifyspringtermdata/CS3DS19.html', springdata=springdata)