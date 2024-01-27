#!/usr/bin/python3
"""
Script starts a Flask web application with a route that displays "Hello HBNB!"
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Function handles the root route ('/') and displays "Hello HBNB!"
    """
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
