#!/usr/bin/python3

"""
Return string when navigating to root dir
"""

from flask import Flask, render_template, g
import models
from models.state import State


app = Flask(__name__, template_folder='templates')


@app.route('/cities_by_states', strict_slashes=False)
def liststatecities():
    """view that lists all cities by their states"""
    states = models.storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(error):
    """remove the current SQLAlchemy Session"""
    models.storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=500)
