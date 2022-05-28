# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'todo101.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItem, QStandardItemModel
import sqlite3 as sql


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(88, 30, 611, 20))
        self.label.setObjectName("label")
        self.textedit1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textedit1.setGeometry(QtCore.QRect(43, 70, 391, 70))
        self.textedit1.setObjectName("textedit1")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(160, 180, 151, 61))
        self.add.setObjectName("add")
        self.listwidget1 = QtWidgets.QListWidget(self.centralwidget)
        self.listwidget1.setGeometry(QtCore.QRect(45, 260, 391, 192))
        self.listwidget1.setObjectName("listwidget1")
        self.remove = QtWidgets.QPushButton(self.centralwidget)
        self.remove.setGeometry(QtCore.QRect(170, 500, 151, 61))
        self.remove.setObjectName("remove")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.conn = sql.connect('todo.db')
        self.c = self.conn.cursor()
        try:
            self.c.execute('''CREATE TABLE LIST101(id INTEGER PRIMARY KEY AUTOINCREMENT, todo VARCHAR(100),state TINYINT)''')
        except:
            print('table exists')
        self.listwidget1.itemClicked.connect(self.completeTask)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def completeTask(self,item):
        f = item.font()
        f.setStrikeOut(True)
        item.setFont(f)
        self.update_task(item)





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "                            TO-DO 101"))
        self.add.setText(_translate("MainWindow", "ADD"))
        self.remove.setText(_translate("MainWindow", "DELETE"))
        self.add.clicked.connect(self.to_add_task)
        self.remove.clicked.connect(self.delete_task)
        self.load_task()

    def to_add_task(self):
        item_name=self.textedit1.toPlainText()
        self.listwidget1.addItem(item_name)
        self.c.execute("INSERT INTO LIST101 VALUES (null,'{}',0)".format(item_name))
        self.conn.commit()
    def load_task(self):
        self.listwidget1.clear()
        results=self.c.execute("SELECT * FROM LIST101")
        if (results):
            for row in results:
                item_name = row[1]
                state = row[2]
                if item_name:
                    if state:
                        self.listwidget1.addItem(item_name+" [done]")
                    else:
                        self.listwidget1.addItem(item_name)
    def delete_task(self):
        list_items=self.listwidget1.selectedItems()
        for y in list_items:
            c=y.text()
            c=c.replace(' [done]','')
            print(c)
            #query="DELETE FROM LIST101 WHERE todo  LIKE '{}'".format(c)
            print(query)
            self.c.execute(query)
            self.conn.commit()
            self.load_task()

    def update_task(self,item):
            c=item.text()
            #self.c.execute("UPDATE LIST101 SET state=1")
            self.c.execute("UPDATE LIST101 SET state=1 WHERE todo  LIKE '{}'".format(c))
            self.conn.commit()
            # self.load_task()

























































if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

