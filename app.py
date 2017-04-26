'''
KraKen the Code webapp
'''

import os
from data_manager import get_user_projects, add_user_project, remove_user_project
from data_manager import get_tasks, add_task, remove_task
from tools import get_random_text
from flask import Flask, request, session, redirect, render_template, url_for, make_response
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/hi')
# def test():
#     d = {'hi': 'hi'}
#     return make_response(json.dumps(d), 200, {'content_type': 'application/json'})


# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name.capitalize() if name else name)


@app.route('/modules')
def module_chooser():
    if request.args.get("usr"):
        print("login: " + request.args.get("usr"))
        session['usr'] = request.args.get("usr")

    return render_template('modules.html')


@app.route('/comMission')
def com_mission_module():
    return render_template('projects.html',
                           projects=get_user_projects(session.get('usr')),
                           add_proj=url_for('add_proj'),
                           back_link=url_for('module_chooser')
                           )


@app.route('/addProject')
def add_proj():
    add_user_project(session.get('usr'), get_random_text(10), get_random_text(20))
    return redirect(url_for('com_mission_module'))


@app.route('/deleteProject')
def del_project():
    proj_id = request.args.get('project_id')
    remove_user_project(session.get('usr'), proj_id)
    return redirect(url_for('com_mission_module'))


@app.route('/project')
def project_page():
    project_id = request.args.get('project_id')
    return render_template('tasks.html',
                           tasks=get_tasks(project_id),
                           add_task='{}?project_id={}'.format(url_for('add_task'), project_id),
                           back_link=url_for('com_mission_module')
                           )


@app.route('/addTask')
def add_task():
    project_id = request.args.get('project_id')
    add_task(project_id, get_random_text(15), 'LOW', 'TODO')
    return redirect('{}?project_id={}'.format(url_for('project_page'), project_id))


@app.route('/deleteTask')
def del_task():
    task_id = request.args.get('task_id')
    project_id = request.args.get('project_id')
    remove_task(project_id, task_id)
    return redirect('{}?project_id={}'.format(url_for('project_page'), project_id))


@app.route('/logout')
def logout():
    print('logout: ' + session['usr'])
    session.pop('usr', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True)
