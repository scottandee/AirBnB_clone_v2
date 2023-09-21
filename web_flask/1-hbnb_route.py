#!/usr/bin/python3
"""This script builds on task 0 and
adds a new route called '/hbnb'
"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """This displays Hello when the
    root is queried
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """This route displays "HBNB"
    when queried
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
