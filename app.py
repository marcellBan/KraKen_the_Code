"""
KraKen the Code webapp
"""

import json
from flask import Flask, render_template, make_response, url_for
app = Flask(__name__)


@app.route("/")
def root():
    return render_template("index.html", main_js=url_for('static', filename='js/main.js'))


# @app.route("/hi")
# def test():
#     d = {"hi": "hi"}
#     return make_response(json.dumps(d), 200, {"content_type": "application/json"})


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html', name=name.capitalize() if name else name)


@app.route("/jazmin")
def jazmin():
    return "Good morning"

if __name__ == "__main__":
    app.run(debug=True)
