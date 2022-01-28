#!/usr/bin/python3

"""
Return string when navigating to root dir
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """Return HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Route /c/<text> returns C message"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text="is cool"):
    """Route /python/(<text>) returns Python message"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == '__main__':                                                                                          
    app.run(host='0.0.0.0', port=5000)
