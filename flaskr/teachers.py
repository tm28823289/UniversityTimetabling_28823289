from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db
from pathlib import Path
import os.path
import json

bp = Blueprint('teachers', __name__)

@bp.route('/teachers', methods=('GET', 'POST'))
def classroom():
    with open('flaskr/input_data/mainfile.json', "r") as d:
        dataTerm = json.load(d)
    return render_template('insertData/teachers.html', dataTerm=dataTerm)