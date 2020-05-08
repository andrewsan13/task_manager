import sys  # нужен для передачи argv в QApplication
import os  # для методов отображения содержимого директорий

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate

import design  # наш файл дизайна


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # нужно для доступа к переменным и методам в файле design.py
        super().__init__()
        self.setupUi(self)  # инициализация нашего дизайна
        self.btnSearch.clicked.connect(self.show_tasks)
        # self.calendarWidget.clicked[QDate].connect(self.show_tasks)
        self.btnCreateTask.clicked.connect(self.create_task)
        self.tasks = {}
        self.projects = {}
        self.btnDeleteProj.clicked.connect(self.show_projects)
        self.btnCreateProj.clicked.connect(self.create_project)
        self.listWidget_Projects.clicked.connect(self.change_action_proj)
        self.calendarWidget.clicked.connect(self.change_action_calendar)
        self.last_action = None

    def change_action_calendar(self):
        self.last_action = "calendar"

    def change_action_proj(self):
        self.last_action = "projects"

    def show_tasks(self):
        self.listWidget_Tasks.clear()

        if self.last_action == 'projects':
            proj = self.listWidget_Projects.selectedItems()[0].text()
            for key in self.projects[proj].keys():
                self.listWidget_Tasks.addItem(self.projects[proj][key])
        else:
            date = self.calendarWidget.selectedDate()
            if self.tasks.get(hash(date)):
                self.listWidget_Tasks.addItem(self.tasks[hash(date)])
            else:
                self.listWidget_Tasks.addItem(' ')

    def create_task(self):
        task, ok = QtWidgets.QInputDialog.getText(self, "Create Task", "Enter task:")
        if self.last_action == 'calendar' or not self.last_action:
            date = self.calendarWidget.selectedDate()
            self.tasks[hash(date)] = task
        else:
            proj = self.listWidget_Projects.selectedItems()[0].text()
            self.projects[proj][hash(task)] = task

    def edit_task(self):
        pass

    def delete_task(self):
        pass

    def show_projects(self):
        self.listWidget_Projects.clear()
        for key in self.projects.keys():
            self.listWidget_Projects.addItem(key)

    def create_project(self):
        proj, ok = QtWidgets.QInputDialog.getText(self, "Create Project", "Enter project name:")
        self.projects[proj] = {}

    def edit_project(self):
        pass

    def delete_project(self):
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()  # Показать окно

    app.exec_()  # запуск приложения


if __name__ == '__main__':
    main()
