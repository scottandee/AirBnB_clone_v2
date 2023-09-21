#!/usr/bin/python3
"""This script starts a simple flask web
application that listens on 0.0.0.0, port 5000
"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """This displays Hello when the
    root is queried
    """

    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
