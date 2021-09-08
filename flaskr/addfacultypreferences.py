from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db
from pathlib import Path
import os.path
import json

bp = Blueprint('addfacultypreferences', __name__)

@bp.route('/addfacultypreferences', methods=('GET', 'POST'))
def addclassroom():
    if request.method == "POST":
        userreq = request.form
        facultyname = userreq.get('teachername')
        nonprefST = float(userreq.get("facultyStartTime"))
        nonprefET = float(userreq.get("facultyEndTime"))
        nonprefRooms = userreq.get('classroom')
        nonprefDays = userreq.get('days')
        a_file = open("flaskr/input_data/mainfile.json", "r")
        json_object = json.load(a_file)
        a_file.close()

        if 'Lecture_time not prefered' not in json_object:
            json_object['Lecture_time not prefered'] = [[facultyname,[nonprefST, nonprefET]]]
        else:
            json_object['Lecture_time not prefered'] += [[facultyname,[nonprefST, nonprefET]]]

        if 'Lecture rooms not prefered by teaching faculty' not in json_object:
            json_object['Lecture rooms not prefered by teaching faculty'] = [[facultyname,[nonprefRooms]]]
        else:
            json_object['Lecture rooms not prefered by teaching faculty'] += [[facultyname,[nonprefRooms]]]

        if 'Teaching days not prefered by teaching faculty' not in json_object:
            json_object['Teaching days not prefered by teaching faculty'] = [[facultyname,[nonprefDays]]]
        else:
            json_object['Teaching days not prefered by teaching faculty'] += [[facultyname,[nonprefDays]]]
        
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    return render_template('insertData/addfacultypreferences.html')



