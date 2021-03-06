from data_types import Task, Project
from flask import url_for
import json
import os


def get_user_projects(user_id):
    pm = ProjectManager(user_id)
    return pm.get_user_projects()


def add_user_project(user_id, title, description):
    pm = ProjectManager(user_id)
    pm.add_user_project(Project(title, description))


def remove_user_project(user_id, project_id):
    pm = ProjectManager(user_id)
    pm.remove_user_project(project_id)


def get_tasks(project_id):
    tm = TaskManager(project_id)
    return tm.get_tasks()


def add_task(project_id, description, priority, status):
    tm = TaskManager(project_id)
    tm.add_task(Task(description, priority, status))


def remove_task(project_id, task_id):
    tm = TaskManager(project_id)
    tm.remove_task(task_id)


class ProjectManager(object):

    def __init__(self, usr_id):
        '''
        loads projects from file
        filename = usr_id + '.db'
        '''
        self.usr_id = usr_id
        self._projects = list()  # list of Project objects loaded from file
        self._fname = 'data/users/{}.db'.format(self.usr_id)
        if os.path.isfile(self._fname):
            self._get_projects_from_file()

    def get_user_projects(self):
        ret = list()
        for proj in self._projects:
            ret.append({
                'proj_name': proj.title,
                'proj_link': '{}?project_id={}'.format(url_for('project_page'), proj.id),
                'del_link': '{}?project_id={}'.format(url_for('del_project'), proj.id)
            })
        return ret

    def add_user_project(self, new_project):
        '''adds a new user project'''
        self._projects.append(new_project)
        self._save_user_projects()

    def remove_user_project(self, project_id):
        '''removes a user project'''
        project_id = int(project_id)
        for i, proj in enumerate(self._projects):
            if proj.id == project_id:
                del(self._projects[i])
                break
        self._save_user_projects()

    def _save_user_projects(self):
        data = {
            'projects': list(map(lambda x: x.get_dict(), self._projects))
        }
        with open(self._fname, 'w') as dbfile:
            json.dump(data, dbfile)

    def _get_projects_from_file(self):
        with open(self._fname) as dbfile:
            data = json.load(dbfile)
        for proj in data.get('projects'):
            self._projects.append(Project(
                proj.get('title'),
                proj.get('description'),
                id=proj.get('id')
            ))


class TaskManager(object):

    def __init__(self, project_id):
        '''
        loads tasks from file
        filename = project_id + '.db'
        '''
        self.project_id = project_id
        self._tasks = list()
        self._fname = 'data/projects/{}.db'.format(self.project_id)
        if os.path.isfile(self._fname):
            self._get_tasks_from_file()

    def get_tasks(self):
        ret = list()
        for task in self._tasks:
            ret.append({
                'task_name': task.description,
                'del_link': '{}?task_id={}&project_id={}'.format(url_for('del_task'), task.id, self.project_id)
            })
        return ret

    def add_task(self, new_task):
        '''adds a new task to the list of tasks and saves the db'''
        self._tasks.append(new_task)
        self._save_db()

    def remove_task(self, task_id):
        '''removes task and saves db'''
        task_id = int(task_id)
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                del(self._tasks[i])
                break
        self._save_db()

    def update_task_priority(self, task_id, new_priority):
        for task in self._tasks:
            if task.id == task_id:
                task.priority = new_priority
                break
        self._save_db()

    def update_task_status(self, task_id, new_status):
        for task in self._tasks:
            if task.id == task_id:
                task.status = new_status
                break
        self._save_db()

    def _save_db(self):
        '''writes the list of tasks to the dbfile'''
        data = {
            'tasks': list(map(lambda x: x.get_dict(), self._tasks))
        }
        with open(self._fname, 'w') as dbfile:
            json.dump(data, dbfile)

    def _get_tasks_from_file(self):
        with open(self._fname) as dbfile:
            data = json.load(dbfile)
        for task in data.get('tasks'):
            self._tasks.append(Task(
                task.get('description'),
                task.get('priority'),
                task.get('status'),
                id=task.get('id')
            ))
