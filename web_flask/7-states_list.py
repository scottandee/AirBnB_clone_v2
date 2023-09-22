#!/usr/bin/python3
"""This script lists all states in
the database storage
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception=None):
    """This removes the current SQLAlchemy session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """List all states in DBStorage"""
    obj = storage.all(State)
    return render_template("7-states_list.html", states=obj)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
