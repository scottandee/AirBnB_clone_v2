#!/usr/bin/python3
"""List States if no id specified, List cities
in state if id specified"""

from flask import Flask, render_template
from markupsafe import escape
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception=None):
    """This removes the current SQLAlchemy session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """List all states in DBStorage"""
    obj = storage.all("State")
    return render_template("9-states.html", states=obj, state_id=None)


@app.route("/states/<id>", strict_slashes=False)
def state_id(id):
    """list the cities of the state id specified"""
    myList = [obj for obj in storage.all("State").values()
              if obj.id == escape(id)]
    if len(myList) == 1:
        state = myList[0]
    else:
        state = None
    return render_template("9-states.html", state_id=id, state=state)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
