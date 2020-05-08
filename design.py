# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(765, 773)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnCreateProj = QtWidgets.QPushButton(self.centralwidget)
        self.btnCreateProj.setObjectName("btnCreateProj")
        self.horizontalLayout.addWidget(self.btnCreateProj)
        self.btnDeleteProj = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeleteProj.setObjectName("btnDeleteProj")
        self.horizontalLayout.addWidget(self.btnDeleteProj)
        self.lineSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.lineSearch.setInputMask("")
        self.lineSearch.setText("")
        self.lineSearch.setObjectName("lineSearch")
        self.horizontalLayout.addWidget(self.lineSearch)
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setObjectName("btnSearch")
        self.horizontalLayout.addWidget(self.btnSearch)
        self.btnCreateTask = QtWidgets.QPushButton(self.centralwidget)
        self.btnCreateTask.setObjectName("btnCreateTask")
        self.horizontalLayout.addWidget(self.btnCreateTask)
        self.btnEditTask = QtWidgets.QPushButton(self.centralwidget)
        self.btnEditTask.setObjectName("btnEditTask")
        self.horizontalLayout.addWidget(self.btnEditTask)
        self.btnDeleteTask = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeleteTask.setObjectName("btnDeleteTask")
        self.horizontalLayout.addWidget(self.btnDeleteTask)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget_Projects = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_Projects.setObjectName("listWidget_Projects")
        self.horizontalLayout_2.addWidget(self.listWidget_Projects)
        self.listWidget_Tasks = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_Tasks.setObjectName("listWidget_Tasks")
        self.horizontalLayout_2.addWidget(self.listWidget_Tasks)
        self.horizontalLayout_2.setStretch(1, 10)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnCreateProj.setText(_translate("MainWindow", "Create"))
        self.btnDeleteProj.setText(_translate("MainWindow", "Delete"))
        self.btnSearch.setText(_translate("MainWindow", "Search"))
        self.btnCreateTask.setText(_translate("MainWindow", "Create"))
        self.btnEditTask.setText(_translate("MainWindow", "Edit"))
        self.btnDeleteTask.setText(_translate("MainWindow", "Delete"))
