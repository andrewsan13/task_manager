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

        self.last_action = None
        self.listWidget_Projects.clicked.connect(self.change_action_proj)
        self.calendarWidget.clicked.connect(self.change_action_calendar)

        self.show_projects()  # Показать проэкты, если есть в базе данных
        self.show_tasks()  # Показать задачи, если есть (дефолт на текущую дату)
        self.calendarWidget.clicked[QDate].connect(self.show_tasks)  # показать задачи при нажатии на дату
        self.listWidget_Projects.clicked.connect(self.show_tasks)  # показать задачи при нажатии на проэкт

        # self.btnSearch.clicked.connect(self.search)
        self.btnDeleteProj.clicked.connect(self.edit_project)
        self.btnCreateTask.clicked.connect(self.create_task)
        self.btnCreateProj.clicked.connect(self.create_project)

    def change_action_calendar(self):
        self.last_action = "calendar"

    def change_action_proj(self):
        self.last_action = "projects"

    def message_error(self, which, what):
        w = QtWidgets.QMessageBox()
        w.setWindowTitle("Error Message")
        w.setText(f"{which} is not {what}.")
        w.exec()

    def create_task(self):
        name, ok1 = QtWidgets.QInputDialog.getText(self, "Name", "Enter a name for the task:")
        if ok1 and name:
            priority, ok2 = QtWidgets.QInputDialog.getItem(self, "Priority", "Choose priority:", Task.listPriority)
            if ok2 and priority:
                if self.last_action == 'calendar' or not self.last_action:
                    date = self.calendarWidget.selectedDate()
                    convertor.addcalendartask(date, name, priority)
                else:
                    proj = self.listWidget_Projects.selectedItems()[0].text()
                    convertor.addprojecttask(proj, name, priority)
            else:
                self.message_error("Task", 'added')
        else:
            self.message_error("Task", 'added')

    def show_tasks(self):
        self.listWidget_Tasks.clear()
        if self.last_action == 'projects':
            proj = self.listWidget_Projects.selectedItems()[0].text()
            for one in convertor.getprojecttask(proj):
                self.listWidget_Tasks.addItem(one.name)
        else:
            date = self.calendarWidget.selectedDate()
            for one in convertor.getcalendartask(date):
                self.listWidget_Tasks.addItem(one.name)

    def edit_task(self):
        pass

    def delete_task(self):
        pass

    def create_project(self):
        name, ok = QtWidgets.QInputDialog.getText(self, "Create Project", "Enter project name:")
        if ok:
            convertor.addproject(name)
        else:
            self.message_error("Project", 'added')
        self.show_projects()

    def show_projects(self):
        self.listWidget_Projects.clear()
        p = convertor.getprojects()
        for project in p:
            self.listWidget_Projects.addItem(project.name)

    def edit_project(self):
        proj = self.listWidget_Projects.selectedItems()[0].text()
        name, ok = QtWidgets.QInputDialog.getText(self, "Create Project", f"Current name: {proj}\nEnter new name:")
        if ok and name:
            convertor.editproject(proj, name)
        else:
            self.message_error('Project', 'update')
        self.show_projects()

    def delete_project(self):
        pass
