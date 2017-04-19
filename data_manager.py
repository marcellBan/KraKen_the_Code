from data_types import Task, Project


class ProjectManager(object):
    def __init__(self, usr_id):
        """
        loads projects from file
        filename = usr_id + ".db"
        """
        self.usr_id = usr_id
        # TODO: load data from file if it exists create it if not
        self._projects = list()  # list of Project objects loaded from file

    def get_user_projects(self):
        return self._projects

    def add_user_project(self, new_project):
        """adds a new user project"""

    def remove_user_project(self, project_id):
        """removes a user project"""

    def _save_user_projects(self):
        pass


class DataManager(object):
    def __init__(self, project_id):
        """
        loads tasks from file
        filename = project_id + ".db"
        """
        self.project_id = project_id
        # TODO: load data from file if it exists create it if not
        self._tasks = list()

    def get_tasks(self):
        """returns a list of Task objects"""
        return self._tasks

    def add_task(self, task):
        """adds a new task to the list of tasks and saves the db"""

    def _save_db(self):
        """writes the list of tasks to the dbfile"""

    def remove_task(self, task_id):
        """removes task and saves db"""

    def update_task_priority(self, task_id, new_priority):
        pass

    def update_task_status(self, task_id, new_status):
        pass
