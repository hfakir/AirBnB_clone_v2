#!/usr/bin/python3
""" 2-Starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ say hello """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ show HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ show variable text """
    return f'C {text.replace("_", " ")}'


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)