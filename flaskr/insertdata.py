from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db
from pathlib import Path
import os.path
import json

bp = Blueprint('insertdata', __name__)

@bp.route('/insertData', methods=('GET', 'POST'))
def insertData():
    if request.method == "POST":
        userreq = request.form
        modulecode= userreq.get('modulecode')
        roomCapacity = userreq.get("capacity")
        faculty = userreq.get('faculty')
        batch = userreq.get('batch')
        modulename = userreq.get('modulename')
        term = userreq.get('term')
        lectureDuration = [int(userreq.get("duration"))]
        lectureFrequency = int(userreq.get("frequency"))
        newDuration = [item for item in lectureDuration for i in range(lectureFrequency)]

        a_file = open("flaskr/input_data/mainfile.json", "r")
        json_object = json.load(a_file)
        a_file.close()

        if 'Modules' not in json_object:
            json_object['Modules'] = [[modulecode.upper(),roomCapacity,newDuration,faculty,[batch],modulename,[term]]]
        else:
            json_object['Modules'] += [[modulecode.upper(),roomCapacity,newDuration,faculty,[batch],modulename,[term]]]
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    return render_template('insertData/insertData.html')



