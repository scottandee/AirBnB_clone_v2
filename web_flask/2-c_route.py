#!/usr/bin/python3
"""This script is based on task 1. The new
route takes input from the client and displays
it on the page
"""

from flask import Flask
from markupsafe import escape


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


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """This displays "C" followed by the
    value of the "text" variable
    """
    return f"C {escape(text)}".replace("_", " ")


if __name__ == '__main__':
    app.run(host="0.0.0.0")
