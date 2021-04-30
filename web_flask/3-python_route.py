#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    """ display "Hello HBNB!" in the route "/" """
    return("Hello HBNB!")


@app.route("/hbnb")
def home_hbnb():
    """  display “HBNB” in route "/hbnb" """
    return("HBNB")


@app.route("/c/<text>")
def argument(text):
    """ display “C ” followed by the value of the text variable """
    text1 = text.replace('_', ' ')
    return("C {}".format(text1))


@app.route("/python/")
@app.route("/python/<text>")
def arg_default(text="is cool"):
    text1 = text.replace('_', ' ')
    return("Python {}".format(text1))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
