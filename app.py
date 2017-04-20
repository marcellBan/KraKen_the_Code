'''
KraKen the Code webapp
'''

import os
from data_manager import TaskManager, ProjectManager
from data_types import Task, Project
from tools import get_random_text
from flask import Flask, request, session, redirect, render_template, url_for, make_response
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           main_js=url_for('static', filename='js/main.js'),
                           tools_js=url_for('static', filename='js/tools.js'),
                           style_css=url_for('static', filename='css/style.css')
                           )


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
    if resuest.args.get('usr'):
        print('login: ' + request.args.get('usr'))
        session['usr'] = request.args.get('usr')

    return render_template('modules.html',
                           main_js=url_for('static', filename='js/main.js'),
                           tools_js=url_for('static', filename='js/tools.js'),
                           logout=url_for('logout'),
                           style_css=url_for('static', filename='css/style.css'),
                           kraken_icon=url_for('static', filename='img/kraken_icon.png'),
                           kraken_logo=url_for('static', filename='img/kraken_logo.png')
                           )


@app.route('/comMission')
def com_mission_module():
    project_manager = ProjectManager(session.get('usr'))
    return render_template('projects.html',
                           projects=project_manager.get_user_projects(),
                           add_proj=url_for('add_proj')
                           back_link=url_for('module_chooser'),
                           logout=url_for('logout'),
                           style_css=url_for('static', filename='css/style.css'),
                           kraken_icon=url_for('static', filename='img/kraken_icon.png'),
                           kraken_logo=url_for('static', filename='img/kraken_logo.png')
                           )


@app.route('/addProject')
def add_proj():
    project_manager = ProjectManager(session.get('usr'))
    project_manager.add_user_project(Project(get_random_text(10), get_random_text(20)))
    return redirect(url_for('com_mission_module'))


@app.route('/deleteProject')
def del_project():
    project_manager = ProjectManager(session.get('usr'))
    proj_id = request.args.get('project_id')
    project_manager.remove_user_project(proj_id)
    return redirect(url_for('com_mission_module'))


@app.route('/project')
def project_page():
    project_id = request.args.get('project_id')
    task_manager = TaskManager(project_id)
    return render_template('tasks.html'
                           tasks=task_manager.get_tasks(),
                           add_task='{}?project_id={}'.format(url_for('add_task'), project_id)
                           back_link=url_for('com_mission_module'),
                           logout=url_for('logout'),
                           style_css=url_for('static', filename='css/style.css'),
                           kraken_icon=url_for('static', filename='img/kraken_icon.png'),
                           kraken_logo=url_for('static', filename='img/kraken_logo.png')
                           )


@app.route('/addTask')
def add_task():
    project_id = request.args.get('project_id')
    task_manager = TaskManager(project_id)
    task_manager.add_task(Task(get_random_text(15), 'LOW', 'TODO'))
    return redirect('{}?project_id={}'.format(url_for('project_page'), project_id))


@app.route('/deleteTask')
def del_task():
    task_id = request.args.get('task_id')
    project_id = request.args.get('project_id')
    task_manager = TaskManager(project_id)
    task_manager.remove_task(task_id)
    return redirect('{}?project_id={}'.format(url_for('project_page'), project_id))


@app.route('/logout')
def logout():
    print('logout: ' + session['usr'])
    session.pop('usr', None)
    return redirect(url_for('root'))


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True)
