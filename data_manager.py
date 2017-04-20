from data_types import Task, Project
import json
import os


class ProjectManager(object):

    def __init__(self, usr_id):
        """
        loads projects from file
        filename = usr_id + ".db"
        """
        self.usr_id = usr_id
        self._projects = list()  # list of Project objects loaded from file
        self._fname = "data/users/{}.db".format(self.usr_id)
        if os.path.isfile(self._fname):
            self._get_projects_from_file()

    def get_user_projects(self):
        return self._projects

    def add_user_project(self, new_project):
        """adds a new user project"""
        self._projects.append(new_project)
        self._save_user_projects()

    def remove_user_project(self, project_id):
        """removes a user project"""
        for i, proj in enumerate(self._projects):
            if proj.id == project_id:
                del(self._projects[i])
                break
        self._save_user_projects()

    def _save_user_projects(self):
        data = {
            "projects": list(map(lambda x: x.get_dict(), self._projects))
        }
        with open(self._fname, "w") as dbfile:
            json.dump(data, dbfile)

    def _get_projects_from_file(self):
        with open(self._fname) as dbfile:
            data = json.load(dbfile)
        for proj in data.get("projects"):
            self._projects.append(
                Project(proj.get("title"),
                        proj.get("description"),
                        id=proj.get("id")))


class TaskManager(object):

    def __init__(self, project_id):
        """
        loads tasks from file
        filename = project_id + ".db"
        """
        self.project_id = project_id
        # TODO: load data from file if it exists create it if not
        self._tasks = list()
        self._fname = "data/projects/{}.db".format(self.project_id)
        if os.path.isfile(self._fname):
            self._get_tasks_from_file()

    def get_tasks(self):
        """returns a list of Task objects"""
        return self._tasks

    def add_task(self, new_task):
        """adds a new task to the list of tasks and saves the db"""
        self._tasks.append(new_task)
        self._save_db()

    def remove_task(self, task_id):
        """removes task and saves db"""
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
        """writes the list of tasks to the dbfile"""
        data = {
            "tasks": list(map(lambda x: x.get_dict(), self._tasks))
        }
        with open(self._fname, "w") as dbfile:
            json.dump(data, dbfile)

    def _get_projects_from_file(self):
        with open(self._fname) as dbfile:
            data = json.load(dbfile)
        for task in data.get("tasks"):
            self._projects.append(
                Task(task.get("description"),
                     task.get("priority"),
                     task.get("status"),
                     id=task.get("id")))
