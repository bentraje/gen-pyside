import sys
# from PyQt5.QtWidgets import QApplication,QMainWindow
# from PyQt5 import uic

from PySide6.QtWidgets import QApplication,QMainWindow,QCheckBox
from PySide6.QtUiTools import loadUiType

import os

qtCreator_menu='mainCode/UiFiles/RunAppUiFile.ui'
Ui_Class_Menu,Qt_Class_menu=loadUiType(qtCreator_menu)

class main_class(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_initUI()

    def main_initUI(self):
        self.ui_main=Ui_Class_Menu()
        self.ui_main.setupUi(self)
        self.ui_main.memo_btn.clicked.connect(lambda: self.memo('mainCode\otextEditor.py'))
        self.ui_main.attn_btn.clicked.connect(lambda: self.attendance('mainCode\oattendance_final.py'))
        self.ui_main.assign_btn.clicked.connect(lambda: self.assignement('mainCode\oassignment.py'))
        self.ui_main.to_do.clicked.connect(lambda: self.todo('mainCode\cal_final.py'))

    def memo(self,name):
        os.system(name)
        # exec(open('textEditor.py').read())

    def attendance(self,name):
        os.system(name)
        # exec(open('attendance_final.py').read())

    def assignement(self,name):
        os.system(name)
        # exec(open('assignment.py').read())

    def todo(self,name):
        os.system(name)
        # exec(open('cal_final.py').read())


app=QApplication(sys.argv)
win=main_class()
win.show()
sys.exit(app.exec_())
