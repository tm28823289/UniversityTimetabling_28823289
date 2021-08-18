from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db
from pathlib import Path
import os.path
import json

bp = Blueprint('selecttimeterm', __name__)

@bp.route('/', methods=('GET', 'POST'))
def selecttimeterm():
    return render_template('modifyInputData/selecttimeterm/selecttimeterm.html')
    
@bp.route('/selecttermdata', methods=('GET', 'POST'))
def selecttermdata():
    if request.method == "POST":
        userreq = request.form
        morningST = float(userreq.get("morningStartTime"))
        morningET = float(userreq.get("morningEndTime"))
        afternoonST = float(userreq.get("afternoonStartTime"))
        afternoonET = float(userreq.get("afternoonEndTime"))
        selecttermdata.term = userreq.get("term")
        selecttermdata.str_path = selecttermdata.term
        selecttermdata.path = Path(selecttermdata.str_path)
        selecttermdata.Qpath = os.path.join('flaskr/input_data/', selecttermdata.path)
        file1 = open(selecttermdata.Qpath, "r")
        file2 = open('flaskr/input_data/mainfile.json', "w")
        l = file1.readline()
        while l:
            file2.write(l)
            l = file1.readline()
        file1.close()
        file2.close()
        a_file = open('flaskr/input_data/mainfile.json', "r")
        json_object = json.load(a_file)
        a_file.close()
        json_object["University time"][0][0] = morningST
        json_object["University time"][0][1] = morningET
        json_object["University time"][1][0] = afternoonST
        json_object["University time"][1][1] = afternoonET
        jsonString = json.dumps(json_object)
        jsonFile = open('flaskr/input_data/mainfile.json', "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        with open('flaskr/input_data/mainfile.json', "r") as d:
            dataTerm = json.load(d)
    elif request.method == "GET":
        with open('flaskr/input_data/mainfile.json', "r") as d:
            dataTerm = json.load(d)
    return render_template('modifyInputData/selecttimeterm/selecttermdata.html', dataTerm=dataTerm)
