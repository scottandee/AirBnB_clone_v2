#!/usr/bin/python3
"""This script builds on 5-number_template.py.
When the new route "/number_odd_or_even/" is
queried it diplays if the user input is even
or odd with its corresponding output
"""

from flask import Flask, render_template
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


@app.route('/python', strict_slashes=False, defaults={"text": "is_cool"})
@app.route('/python/<text>', strict_slashes=False)
def display_py(text):
    """This displays "Python followed by the
    value of the "text" variable
    """
    return f"Python {escape(text)}".replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """This function gives an output only if
    the user input is an integer value
    """
    return f"{escape(n)} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def render_number(n):
    """This function displays an html page if
    `n` is an integer
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_odd(n):
    """This function displays a html page if
    `n` is an integer. During rendering, it also
    checks if the number is even or odd
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
