
class Task(object):
    def __init__(self, description, priority, status, id=None):
        self.description = description
        self.priority = priority
        self.status = status
        if id is not None:
            self.id = id
        else:
            self.id = 1  # generate somehow


class Project(object):
    def __init__(self, title, description, id=None):
        self.title = title
        self.description = description
        if id is not None:
            self.id = id
        else:
            self.id = 1  # generate somehow

    def get_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description
        }
