
class Task(object):
    def __init__(self, description, priority, status):
        self.description = description
        self.priority = priority
        self.status = status
        self.id = pass  # generate somehow


class Project(object):
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.id = pass  # generate somehow
