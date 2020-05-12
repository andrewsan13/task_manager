from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate

import design  # наш файл дизайна
from models import Task
import convertor


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # нужно для доступа к переменным и методам в файле design.py
        super().__init__()
        self.setupUi(self)  # инициализация нашего дизайна
        self.btnSearch.clicked.connect(self.show_tasks)
        # self.calendarWidget.clicked[QDate].connect(self.show_tasks)
        self.btnCreateTask.clicked.connect(self.create_task)
        self.btnDeleteProj.clicked.connect(self.show_projects)
        self.btnCreateProj.clicked.connect(self.create_project)
        self.listWidget_Projects.clicked.connect(self.change_action_proj)
        self.calendarWidget.clicked.connect(self.change_action_calendar)
        self.last_action = None

    def change_action_calendar(self):
        self.last_action = "calendar"

    def change_action_proj(self):
        self.last_action = "projects"

    def create_task(self):
        name, ok1 = QtWidgets.QInputDialog.getText(self, "Name", "Enter a name for the task:")
        priority, ok2 = QtWidgets.QInputDialog.getItem(self, "Priority", "Choose priority:", Task.getPriority())
        if ok1 and ok2 and name and priority:
            new_task = Task(name, priority)
            if self.last_action == 'calendar' or not self.last_action:
                date = self.calendarWidget.selectedDate()
            else:
                proj = self.listWidget_Projects.selectedItems()[0].text()
        else:
            w = QtWidgets.QMessageBox()
            w.setWindowTitle("Error Message")
            w.setText("Task is not added.")
            w.exec()

    def show_tasks(self):
        self.listWidget_Tasks.clear()

        if self.last_action == 'projects':
            proj = self.listWidget_Projects.selectedItems()[0].text()
            for one in database.fptask(proj):
                p = pickle.loads(one['task'])
                self.listWidget_Tasks.addItem(p.showTaskName())
        else:
            date = self.calendarWidget.selectedDate()
            for one in database.fctask(date):
                p = pickle.loads(one['task'])
                self.listWidget_Tasks.addItem(p.showTaskName())

    def edit_task(self):
        pass

    def delete_task(self):
        pass

    def create_project(self):
        name, ok = QtWidgets.QInputDialog.getText(self, "Create Project", "Enter project name:")
        if ok:
            convertor.addproject(name)
        else:
            w = QtWidgets.QMessageBox()
            w.setWindowTitle("Error Message")
            w.setText("Project is not added.")
            w.exec()

    def show_projects(self):
        self.listWidget_Projects.clear()
        p = convertor.getprojects()
        for project in p:
            self.listWidget_Projects.addItem(project.getName())

    def edit_project(self):
        pass

    def delete_project(self):
        pass
