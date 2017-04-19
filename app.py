"""
KraKen the Code webapp
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def root():
    return "Hello World!"


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html', name=name.capitalize() if name else name)


@app.route("/jazmin")
def jazmin():
    return "Good morning"

if __name__ == "__main__":
    app.run(debug=True)
