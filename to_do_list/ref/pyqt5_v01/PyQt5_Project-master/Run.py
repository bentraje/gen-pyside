import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QCheckBox
from PyQt5 import uic
import os

qtCreator='mainCode/UiFiles/login.ui'
Ui_MainWindow,qt_BaseClass=uic.loadUiType(qtCreator)

class login_form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login_initUI()

    def login_initUI(self):
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.yes_btn.clicked.connect(lambda: self.yes('mainCode\subject.py'))
        self.ui.no_btn.clicked.connect(lambda: self.no('mainCode\RunApp.py'))

    def no(self,name):
        os.system(name)
    def yes(self,name):
        os.system(name)
        checkbox=QCheckBox()
        checkbox.setText('Data saved properly')
        self.ui.fLayout.addWidget(checkbox)
        checkbox.stateChanged.connect(self.dataSaved)

    def dataSaved(self):
        print('yeah')
        exec(open('mainCode\RunApp.py').read())


app=QApplication(sys.argv)
win=login_form()
win.show()
sys.exit(app.exec_())