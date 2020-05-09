class Project:
    def __init__(self, name):
        self.name: str = name

    def showProjectName(self):
        return self.name

    def addTask(self, task):
        self.tasks.append(task)


class Calendar:
    def __init__(self, date):
        self.date = date

    def showCalendarDate(self):
        return self.date

    def addTask(self, task):
        self.tasks.append(task)


class Task:
    listPriority = ('Regular', 'Hot', 'Lazy')
    listStatus = ('In progress', 'Done')

    def __init__(self, name, priority, status='In progress'):
        self.name: str = name
        self.status: str = status
        self.priority: str = priority

    @classmethod
    def getPriority(cls):
        return cls.listPriority

    @classmethod
    def getStatus(cls):
        return cls.listStatus

    def showTaskName(self):
        return self.name

    def showTaskStatus(self):
        return self.status

    def showTaskPriority(self):
        return self.priority
