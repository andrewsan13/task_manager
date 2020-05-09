class Project:
    def __init__(self, name):
        self.name: str = name
        self.tasks = []

    def showProjectName(self):
        return self.name

    def showProjectTasks(self):
        return self.tasks

    def newTask(self, name, status, priority):
        new = Task(name, status, priority)
        self.tasks.append(new)
        return new


class Calendar:
    def __init__(self, date):
        self.date = date
        self.tasks = []

    def showCalendarDate(self):
        return self.date

    def showCalendarTasks(self):
        return self.tasks

    def newTask(self, name, status, priority):
        new = Task(name, status, priority)
        self.tasks.append(new)
        return new


class Task:
    def __init__(self, name, status, priority):
        self.name: str = name
        self.status: str = status
        self.priority: str = priority
