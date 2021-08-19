from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db
from pathlib import Path
import os.path
import json


with open("flaskr/output_data/final_data.json", "r") as a:
    final_data = json.load(a)

bp = Blueprint('viewTimetableSchedule', __name__)

@bp.route('/timetableSchedule', methods=('GET', 'POST'))
def select_batch():
	if request.method == "POST":
		req = request.form
		batch = req.get("batch")
		str_path = batch
		path = Path(str_path)
		Qpath = os.path.join('flaskr/output_data/', path)
		with open(Qpath, "r") as d:
			data = json.load(d)
	return render_template('viewData/timetableSchedule.html', data_dict=data)

@bp.route("/CSMBD16.html")
def CSMBD16():
    return render_template('viewData/CSMBD16.html', data_dict=final_data)

@bp.route("/CS3AI18-CSMAI19.html")
def CS3AI18_CSMAI19():
    return render_template('viewData/CS3AI18-CSMAI19.html', data_dict=final_data)

@bp.route("/MMM077.html")
def MMM077():
    return render_template('viewData/MMM077.html', data_dict=final_data)

@bp.route("/CSMML16.html")
def CSMML16():
    return render_template('viewData/CSMML16.html', data_dict=final_data)

@bp.route("/CSMRS16.html")
def CSMRS16():
    return render_template('viewData/CSMRS16.html', data_dict=final_data)

@bp.route("/CS3VI18.html")
def CS3VI18():
    return render_template('viewData/CS3VI18.html', data_dict=final_data)

@bp.route("/CS3VR16.html")
def CS3VR16():
    return render_template('viewData/CS3VR16.html', data_dict=final_data)

@bp.route("/CSMIA19.html")
def CSMIA19():
    return render_template('viewData/CSMIA19.html', data_dict=final_data)

@bp.route("/INMR93.html")
def INMR93():
    return render_template('viewData/INMR93.html', data_dict=final_data)

@bp.route("/INMR89.html")
def INMR89():
    return render_template('viewData/INMR89.html', data_dict=final_data)

@bp.route("/INMR77.html")
def INMR77():
    return render_template('viewData/INMR77.html', data_dict=final_data)

@bp.route("/INMR86.html")
def INMR86():
    return render_template('viewData/INMR86.html', data_dict=final_data)

@bp.route("/INMR96.html")
def INMR96():
    return render_template('viewData/INMR96.html', data_dict=final_data)

@bp.route("/INMR65.html")
def INMR65():
    return render_template('viewData/INMR65.html', data_dict=final_data)

@bp.route("/MA1LA.html")
def MA1LA():
    return render_template('viewData/MA1LA.html', data_dict=final_data)

@bp.route("/MA1FM.html")
def MA1FM():
    return render_template('viewData/MA1FM.html', data_dict=final_data)

@bp.route("/MA1CA.html")
def MA1CA():
    return render_template('viewData/MA1CA.html', data_dict=final_data)

@bp.route("/CS1FC16.html")
def CS1FC16():
    return render_template('viewData/CS1FC16.html', data_dict=final_data)

@bp.route("/ST1PS.html")
def ST1PS():
    return render_template('viewData/ST1PS.html', data_dict=final_data)

@bp.route("/MA2RCA.html")
def MA2RCA():
    return render_template('viewData/MA2RCA.html', data_dict=final_data)

@bp.route("/MA2MPR.html")
def MA2MPR():
    return render_template('viewData/MA2MPR.html', data_dict=final_data)

@bp.route("/MA2NAN.html")
def MA2NAN():
    return render_template('viewData/MA2NAN.html', data_dict=final_data)

@bp.route("/MA2DE.html")
def MA2DE():
    return render_template('viewData/MA2DE.html', data_dict=final_data)

@bp.route("/CS2JA16.html")
def CS2JA16():
    return render_template('viewData/CS2JA16.html', data_dict=final_data)

@bp.route("/CS2AO17.html")
def CS2AO17():
    return render_template('viewData/CS2AO17.html', data_dict=final_data)

@bp.route("/MA3NAT.html")
def MA3NAT():
    return render_template('viewData/MA3NAT.html', data_dict=final_data)

@bp.route("/CS3DS19.html")
def CS3DS19():
    return render_template('viewData/CS3DS19.html', data_dict=final_data)

@bp.route("/CSMCC16.html")
def CSMCC16():
    return render_template('viewData/CSMCC16.html', data_dict=final_data)

@bp.route("/CSMDM16.html")
def CSMDM16():
    return render_template('viewData/CSMDM16.html', data_dict=final_data)

@bp.route("/CS3PP19.html")
def CS3PP19():
    return render_template('viewData/CS3PP19.html', data_dict=final_data)

@bp.route("/CSMMA16.html")
def CSMMA16():
    return render_template('viewData/CSMMA16.html', data_dict=final_data)

@bp.route("/INMR95.html")
def INMR95():
    return render_template('viewData/INMR95.html', data_dict=final_data)

@bp.route("/INMR66.html")
def INMR66():
    return render_template('viewData/INMR66.html', data_dict=final_data)

@bp.route("/INMR91.html")
def INMR91():
    return render_template('viewData/INMR91.html', data_dict=final_data)

@bp.route("/INMR94.html")
def INMR94():
    return render_template('viewData/INMR94.html', data_dict=final_data)

@bp.route("/MA2VC.html")
def MA2VC():
    return render_template('viewData/MA2VC.html', data_dict=final_data)

@bp.route("/MA2PSM.html")
def MA2PSM():
    return render_template('viewData/MA2PSM.html', data_dict=final_data)

@bp.route("/CS3DP19.html")
def CS3DP19():
    return render_template('viewData/CS3DP19.html', data_dict=final_data)