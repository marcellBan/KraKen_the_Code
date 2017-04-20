"""
KraKen the Code webapp
"""

import sys
from data_manager import TaskManager, ProjectManager
from data_types import Task, Project
from flask import Flask, request, session, redirect, render_template, url_for, make_response
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html",
                           main_js=url_for('static', filename='js/main.js'),
                           tools_js=url_for('static', filename='js/tools.js'),
                           style_css=url_for('static', filename='css/style.css')
                           )


# @app.route("/hi")
# def test():
#     d = {"hi": "hi"}
#     return make_response(json.dumps(d), 200, {"content_type": "application/json"})


# @app.route("/hello/")
# @app.route("/hello/<name>")
# def hello(name=None):
#     return render_template('hello.html', name=name.capitalize() if name else name)


@app.route("/modules")
def module_chooser():
    if resuest.args.get("usr"):
        print("login: " + request.args.get("usr"))
        session['usr'] = request.args.get("usr")

    return render_template('modules.html',
                           main_js=url_for('static', filename='js/main.js'),
                           tools_js=url_for('static', filename='js/tools.js'),
                           logout=url_for('logout'),
                           style_css=url_for('static', filename='css/style.css')
                           )


@app.route("/comMission")
def com_mission_module():
    session.pop('project_id', None)
    project_manager = ProjectManager(session.get("usr"))
    return render_template('projects.html',
                           projects=project_manager.get_user_projects(),
                           back_link=url_for('module_chooser'),
                           logout=url_for('logout'),
                           style_css=url_for('static', filename='css/style.css')
                           )


@app.route("/project")
def project_page():
    task_manager = TaskManager(request.args.get("project_id"))
    return render_template('tasks.html'
                           tasks=task_manager.get_tasks(),
                           back_link=url_for('comMission'),
                           logout=url_for('logout'),
                           style_css=url_for('static', filename='css/style.css')
                           )


@app.route("/logout")
def logout():
    print("logout: " + session['usr'])
    session.pop('usr', None)
    session.pop('project_id', None)
    return redirect(url_for('root'))


if __name__ == "__main__":
    # TODO: remove this
    app.secret_key = 'test'
    app.run(debug=True)
