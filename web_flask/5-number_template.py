#!/usr/bin/python3
""" 5-Starts a Flask web application """

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """say hello"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """show HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """show variable text"""
    return f'C {text.replace("_", " ")}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is_cool'):
    """show variable text"""
    return f'Python{text.replace("_", " ")}'


@app.route('/number/<int:n>')
def check_integer(n):
    """show only integers"""
    return (f"{n} is a number")


@app.route('/number_template/<int:n>')
def number_template(n):
    """show only integers"""
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)