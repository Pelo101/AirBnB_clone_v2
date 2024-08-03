#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """returns welcome message"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns display message"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    """Displays text"""
    fmt_txt = text.replace('_', ' ')
    return "C {}".format(fmt_txt)


@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """Displays text"""
    pt_text = text.replace('_', ' ')
    return "Python {}".format(pt_text)


@app.route('/python', strict_slashes=False)
def python_default():
    """Displays python default text"""
    default_text = 'is cool'
    return "Python {}".format(default_text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Prints integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_templates(n):
    """Displays templates"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>',  strict_slashes=False)
def odd_even(n):
    """Display html template"""
    if n % 2 == 0:
        OddEven = 'even'

    else:
        OddEven = 'odd'

    return render_template('6-number_odd_or_even.html', n=n, OddEven=OddEven)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
