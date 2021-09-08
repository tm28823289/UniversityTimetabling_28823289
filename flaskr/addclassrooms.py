from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db
from pathlib import Path
import os.path
import json

bp = Blueprint('addclassrooms', __name__)

@bp.route('/addclassrooms', methods=('GET', 'POST'))
def addclassroom():
    if request.method == "POST":
        userreq = request.form
        classroom = userreq.get('room')
        roomCapacity = userreq.get("capacity")
        a_file = open("flaskr/input_data/mainfile.json", "r")
        json_object = json.load(a_file)
        a_file.close()

        if 'Lecturerooms' not in json_object:
            json_object['Lecturerooms'] = [[classroom.upper(),roomCapacity]]
        else:
            json_object['Lecturerooms'] += [[classroom.upper(),roomCapacity]]
        jsonString = json.dumps(json_object)
        jsonFile = open("flaskr/input_data/mainfile.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    return render_template('insertData/addclassrooms.html')



