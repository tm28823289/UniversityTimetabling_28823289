import os
from flask import Flask
from . import db
from . import auth
from . import selecttimeterm
from . import modifySpringTermData
from . import modifyAutumnTermData
from . import z3scheduler
from . import viewTimetableSchedule
from z3 import *


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
	
	
    db.init_app(app)

    app.register_blueprint(auth.bp)
    
    app.register_blueprint(selecttimeterm.bp)
    app.add_url_rule('/', endpoint='modifyInputData.selecttimeterm.selecttimeterm')
    app.add_url_rule('/selecttermdata', endpoint='modifyInputData.selecttimeterm.selecttermdata')
    
    app.register_blueprint(modifySpringTermData.bp)
    app.add_url_rule('/CS3AI18-CSMAI19', endpoint='modifyInputData.modifyspringtermdata.CS3AI18-CSMAI19')
    app.add_url_rule('/MMM077', endpoint='modifyInputData.modifyspringtermdata.MMM077')
    app.add_url_rule('/CSMBD16', endpoint='modifyInputData.modifyspringtermdata.CSMBD16')
    app.add_url_rule('/CSMML16', endpoint='modifyInputData.modifyspringtermdata.CSMML16')
    app.add_url_rule('/CS3VI18', endpoint='modifyInputData.modifyspringtermdata.CS3VI18')
    app.add_url_rule('/CS3VR16', endpoint='modifyInputData.modifyspringtermdata.CS3VR16')
    app.add_url_rule('/CSMIA19', endpoint='modifyInputData.modifyspringtermdata.CSMIA19')
    app.add_url_rule('/INMR93', endpoint='modifyInputData.modifyspringtermdata.INMR93')
    app.add_url_rule('/INMR89', endpoint='modifyInputData.modifyspringtermdata.INMR89')
    app.add_url_rule('/INMR77', endpoint='modifyInputData.modifyspringtermdata.INMR77')
    app.add_url_rule('/INMR86', endpoint='modifyInputData.modifyspringtermdata.INMR86')
    app.add_url_rule('/INMR96', endpoint='modifyInputData.modifyspringtermdata.INMR96')
    app.add_url_rule('/INMR65', endpoint='modifyInputData.modifyspringtermdata.INMR65')
    app.add_url_rule('/MA1LA', endpoint='modifyInputData.modifyspringtermdata.MA1LA')
    app.add_url_rule('/MA1FM', endpoint='modifyInputData.modifyspringtermdata.MA1FM')
    app.add_url_rule('/MA1CA', endpoint='modifyInputData.modifyspringtermdata.MA1CA')
    app.add_url_rule('/CS1FC16', endpoint='modifyInputData.modifyspringtermdata.CS1FC16')
    app.add_url_rule('/ST1PS', endpoint='modifyInputData.modifyspringtermdata.ST1PS')
    app.add_url_rule('/MA2RCA', endpoint='modifyInputData.modifyspringtermdata.MA2RCA')
    app.add_url_rule('/MA2MPR', endpoint='modifyInputData.modifyspringtermdata.MA2MPR')
    app.add_url_rule('/MA2NAN', endpoint='modifyInputData.modifyspringtermdata.MA2NAN')
    app.add_url_rule('/MA2DE', endpoint='modifyInputData.modifyspringtermdata.MA2DE')
    app.add_url_rule('/CS2JA16', endpoint='modifyInputData.modifyspringtermdata.CS2JA16')
    app.add_url_rule('/CS2AO17', endpoint='modifyInputData.modifyspringtermdata.CS2AO17')
    app.add_url_rule('/MA3NAT', endpoint='modifyInputData.modifyspringtermdata.MA3NAT')
    app.add_url_rule('/CS3DS19', endpoint='modifyInputData.modifyspringtermdata.CS3DS19')

    app.register_blueprint(modifyAutumnTermData.bp)
    app.add_url_rule('/CSMCC16', endpoint='modifyInputData.modifyautumntermdata.CSMCC16')
    app.add_url_rule('/CSMDM16', endpoint='modifyInputData.modifyautumntermdata.CSMDM16')
    app.add_url_rule('/CSMMA16', endpoint='modifyInputData.modifyautumntermdata.CSMMA16')
    app.add_url_rule('/CS3PP19', endpoint='modifyInputData.modifyautumntermdata.CS3PP19')
    app.add_url_rule('/CSMRS16', endpoint='modifyInputData.modifyautumntermdata.CSMRS16')
    app.add_url_rule('/INMR95', endpoint='modifyInputData.modifyautumntermdata.INMR95')
    app.add_url_rule('/INMR66', endpoint='modifyInputData.modifyautumntermdata.INMR66')
    app.add_url_rule('/INMR91', endpoint='modifyInputData.modifyautumntermdata.INMR91')
    app.add_url_rule('/INMR94', endpoint='modifyInputData.modifyautumntermdata.INMR94')
    app.add_url_rule('/MA2VC', endpoint='modifyInputData.modifyautumntermdata.MA2VC')
    app.add_url_rule('/MA2PSM', endpoint='modifyInputData.modifyautumntermdata.MA2PSM')
    app.add_url_rule('/CS3DP19', endpoint='modifyInputData.modifyautumntermdata.CS3DP19')

    app.register_blueprint(z3scheduler.bp)
    app.add_url_rule('/run-z3solver', endpoint='viewData.timetableSchedule')

    app.register_blueprint(viewTimetableSchedule.bp)
    app.add_url_rule('/timetableSchedule', endpoint='viewData.timetableSchedule')
    app.add_url_rule('/CSMBD16.html', endpoint='viewData.CSMBD16.html')
    app.add_url_rule('/CS3AI18-CSMAI19.html', endpoint='viewData.CS3AI18-CSMAI19.html')
    app.add_url_rule('/MMM077.html', endpoint='viewData.MMM077.html')
    app.add_url_rule('/CSMML16.html', endpoint='viewData.CSMML16.html')
    app.add_url_rule('/CSMRS16.html', endpoint='viewData.CSMRS16.html')
    app.add_url_rule('/CS3VI18.html', endpoint='viewData.CS3VI18.html')
    app.add_url_rule('/CS3VR16.html', endpoint='viewData.CS3VR16.html')
    app.add_url_rule('/CSMIA19.html', endpoint='viewData.CSMIA19.html')
    app.add_url_rule('/INMR93.html', endpoint='viewData.INMR93.html')
    app.add_url_rule('/INMR89.html', endpoint='viewData.INMR89.html')
    app.add_url_rule('/INMR77.html', endpoint='viewData.INMR77.html')
    app.add_url_rule('/INMR86.html', endpoint='viewData.INMR86.html')
    app.add_url_rule('/INMR96.html', endpoint='viewData.INMR96.html')
    app.add_url_rule('/INMR65.html', endpoint='viewData.INMR65.html')
    app.add_url_rule('/MA1LA.html', endpoint='viewData.MA1LA.html')
    app.add_url_rule('/MA1FM.html', endpoint='viewData.MA1FM.html')
    app.add_url_rule('/MA1CA.html', endpoint='viewData.MA1CA.html')
    app.add_url_rule('/CS1FC16.html', endpoint='viewData.CS1FC16.html')
    app.add_url_rule('/ST1PS.html', endpoint='viewData.ST1PS.html')
    app.add_url_rule('/MA2RCA.html', endpoint='viewData.MA2RCA.html')
    app.add_url_rule('/MA2MPR.html', endpoint='viewData.MA2MPR.html')
    app.add_url_rule('/MA2NAN.html', endpoint='viewData.MA2NAN.html')
    app.add_url_rule('/MA2DE.html', endpoint='viewData.MA2DE.html')
    app.add_url_rule('/CS2JA16.html', endpoint='viewData.CS2JA16.html')
    app.add_url_rule('/CS2AO17.html', endpoint='viewData.CS2AO17.html')
    app.add_url_rule('/MA3NAT.html', endpoint='viewData.MA3NAT.html')
    app.add_url_rule('/CS3DS19.html', endpoint='viewData.CS3DS19.html')
    app.add_url_rule('/CSMCC16.html', endpoint='viewData.CSMCC16.html')
    app.add_url_rule('/CSMDM16.html', endpoint='viewData.CSMDM16.html')
    app.add_url_rule('/CS3PP19.html', endpoint='viewData.CS3PP19.html')
    app.add_url_rule('/CSMMA16.html', endpoint='viewData.CSMMA16.html')
    app.add_url_rule('/INMR95.html', endpoint='viewData.INMR95.html')
    app.add_url_rule('/INMR66.html', endpoint='viewData.INMR66.html')
    app.add_url_rule('/INMR91.html', endpoint='viewData.INMR91.html')
    app.add_url_rule('/INMR94.html', endpoint='viewData.INMR94.html')
    app.add_url_rule('/MA2VC.html', endpoint='viewData.MA2VC.html')
    app.add_url_rule('/MA2PSM.html', endpoint='viewData.MA2PSM.html')
    app.add_url_rule('/CS3DP19.html', endpoint='viewData.CS3DP19.html')

    return app