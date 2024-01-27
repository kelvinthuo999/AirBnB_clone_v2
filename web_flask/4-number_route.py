#!/usr/bin/python3
"""
Script to start a flask web application and handle four routes
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_root():
    """
    Function to handle the root route '/'
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Function to handle the route '/HBNB'
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """
    Function to handle '/c/<text>' route
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def display_python(text='is cool'):
    """
    Function to display python text and handle '/python/' route
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """
    Function to display number and handle '/number/' route
    """
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
