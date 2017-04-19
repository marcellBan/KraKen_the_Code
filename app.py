"""
KraKen the Code webapp
"""

import json
from data_manager import DataManager
from data_types import Task, Project
from flask import Flask, request, session, redirect, render_template, url_for, make_response
app = Flask(__name__)


@app.route("/")
def root():
    return render_template("index.html",
                           main_js=url_for('static', filename='js/main.js'),
                           tools_js=url_for('static', filename='js/tools.js'))


# @app.route("/hi")
# def test():
#     d = {"hi": "hi"}
#     return make_response(json.dumps(d), 200, {"content_type": "application/json"})


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html', name=name.capitalize() if name else name)


@app.route("/modules")
def module_chooser():
    if resuest.args.get("usr"):
        print("login: " + request.args.get("usr"))
        session['usr'] = request.args.get("usr")

    return render_template('modules.html',
                           main_js=url_for('static', filename='js/main.js'),
                           tools_js=url_for('static', filename='js/tools.js'),
                           logout=url_for('logout'))


@app.route("/logout")
def logout():
    print("logout: " + session['usr'])
    session.pop('usr', None)
    return redirect(url_for('root'))


if __name__ == "__main__":
    # TODO: remove this
    app.secret_key = 'test'
    app.run(debug=True)
