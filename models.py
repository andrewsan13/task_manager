class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = {}

    def getName(self):
        return self.name

    def addtask(self, task):
        self.tasks[task.getName()] = task

    def delete(self, task):
        del self.tasks[task.getName()]

class Calendar:
    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date


class Task:
    listPriority = ('Regular', 'Hot', 'Lazy')
    listStatus = ('In progress', 'Done')

    def __init__(self, name, priority, status='In progress'):
        self.name = name
        self.status = status
        self.priority = priority

    @classmethod
    def getlistP(cls):
        return cls.listPriority

    @classmethod
    def getlistS(cls):
        return cls.listStatus

    def getName(self):
        return self.name

    def getStatus(self):
        return self.status

    def getPriority(self):
        return self.priority
