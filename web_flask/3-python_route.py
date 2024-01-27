#!/usr/bin/python3
"""
Script that starts a flask web application and handles four routes
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_root():
    """
    Function to handle the root route
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Function to handle the '/hbnb' route
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """
    Function to handle the '/c' route
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def display_python_text(text='is cool'):
    """
    Function to handle the '/python' route with different variables
    """
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
