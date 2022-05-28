# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'todo2.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(551, 475)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/iconfinder_document-03_1622833.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        MainWindow.setIconSize(QtCore.QSize(25, 25))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addbtn = QtWidgets.QPushButton(self.centralwidget)
        self.addbtn.setGeometry(QtCore.QRect(0, 50, 181, 91))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.addbtn.setFont(font)
        self.addbtn.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #323232);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/iconfinder_icon-33-clipboard-add_315154.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addbtn.setIcon(icon1)
        self.addbtn.setIconSize(QtCore.QSize(25, 25))
        self.addbtn.setObjectName("addbtn")
        self.deletebtn = QtWidgets.QPushButton(self.centralwidget)
        self.deletebtn.setGeometry(QtCore.QRect(0, 130, 181, 91))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.deletebtn.setFont(font)
        self.deletebtn.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #323232);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/iconfinder_draw-08_725558.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deletebtn.setIcon(icon2)
        self.deletebtn.setIconSize(QtCore.QSize(25, 25))
        self.deletebtn.setObjectName("deletebtn")
        self.clearallbtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearallbtn.setGeometry(QtCore.QRect(0, 210, 181, 91))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.clearallbtn.setFont(font)
        self.clearallbtn.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #323232);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/iconfinder_trash_4696642.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearallbtn.setIcon(icon3)
        self.clearallbtn.setIconSize(QtCore.QSize(25, 25))
        self.clearallbtn.setObjectName("clearallbtn")
        self.savebtn = QtWidgets.QPushButton(self.centralwidget)
        self.savebtn.setGeometry(QtCore.QRect(0, 300, 181, 91))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.savebtn.setFont(font)
        self.savebtn.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #323232);\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/iconfinder_simpline_53_2305609.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.savebtn.setIcon(icon4)
        self.savebtn.setIconSize(QtCore.QSize(25, 25))
        self.savebtn.setObjectName("savebtn")
        self.loadbtn = QtWidgets.QPushButton(self.centralwidget)
        self.loadbtn.setGeometry(QtCore.QRect(0, 390, 181, 91))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.loadbtn.setFont(font)
        self.loadbtn.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #323232);\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/iconfinder_Open_1493293.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loadbtn.setIcon(icon5)
        self.loadbtn.setIconSize(QtCore.QSize(25, 25))
        self.loadbtn.setObjectName("loadbtn")
        self.todolist = QtWidgets.QListWidget(self.centralwidget)
        self.todolist.setGeometry(QtCore.QRect(180, 0, 371, 481))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.todolist.setFont(font)
        self.todolist.setStyleSheet("\n"
"\n"
"QListWidget::item {\n"
"    color:white;\n"
"\n"
"}\n"
"\n"
"QListWidget::item:selected{\n"
"   color:white;\n"
"    \n"
"    background-color: rgb(34, 104, 51);\n"
"\n"
"}")
        self.todolist.setObjectName("todolist")
        self.addlist = QtWidgets.QLineEdit(self.centralwidget)
        self.addlist.setGeometry(QtCore.QRect(0, 0, 181, 51))
        self.addlist.setStyleSheet("border: 1px solid gray;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(30,30,30);")
        self.addlist.setObjectName("addlist")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToDo List"))
        self.addbtn.setText(_translate("MainWindow", "加入項目"))
        self.deletebtn.setText(_translate("MainWindow", "清除所選項目"))
        self.clearallbtn.setText(_translate("MainWindow", "清除全部項目"))
        self.savebtn.setText(_translate("MainWindow", "存取清單\n"
"(Ctrl+S)"))
        self.loadbtn.setText(_translate("MainWindow", "讀取清單\n"
"(Ctrl+F)"))


import image_rc