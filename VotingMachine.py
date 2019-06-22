from flask import Flask
from multiprocessing import Pool
import os
import logging
from logging.handlers import RotatingFileHandler

if not os.path.exists("databases"):
    os.makedirs("databases")

app = Flask(__name__)
app.draw = (False, None, None)

if __name__ == '__main__':
    app.pool = Pool(processes=1)
    from blueprints.blueprints_voters import url_voter
    from blueprints.blueprints_coordinator import url_coordinator

    logHandler = RotatingFileHandler('info.log', maxBytes=1000000000, backupCount=1)

    # set the log handler level
    logHandler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    logHandler.setFormatter(formatter)
    # set the app logger level
    app.logger.setLevel(logging.INFO)

    app.logger.addHandler(logHandler)

    app.register_blueprint(url_voter)
    app.register_blueprint(url_coordinator)
    app.run()
