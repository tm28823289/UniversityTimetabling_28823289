from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db
from pathlib import Path
import os.path
import json

bp = Blueprint('landingpage', __name__)

@bp.route('/landingpage', methods=('GET', 'POST'))
def landingpage():
    return render_template('landingpage/landingpage.html')
    