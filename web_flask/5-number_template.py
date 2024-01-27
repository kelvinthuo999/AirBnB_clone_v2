#!/usr/bin/python3
"""
Script starts a Flask web application with six routes
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This function handles the root route ('/') and displays "Hello HBNB!"
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    This function handles the '/hbnb' route and displays "HBNB"
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """
    This function handles the '/c/<text>' route and displays "C "
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text='is cool'):
    """
    Function handles the '/python/<text>' route
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """
    Function handles the '/number/<n>' route
    """
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """
    Function handles the '/number_template/<n>' route and displays an HTML page
    only if n is an integer.
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
