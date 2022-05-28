import sys
#from PyQt5.QtWidgets import QMainWindow,QApplication,qApp
#from PyQt5 import uic

from PySide6.QtWidgets import QApplication,QMainWindow,QCheckBox
from PySide6.QtUiTools import loadUiType

qtCreator='mainCode/UiFiles/sub_attd.ui'
Ui_MainWindow,Qt_BaseClass=loadUiType(qtCreator)

class save_attd(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.save_btn.clicked.connect(self.save)


    def save(self):
        sub1=self.ui.line1.text()
        sub2=self.ui.line2.text()
        sub3=self.ui.line3.text()
        sub4=self.ui.line4.text()
        sub5=self.ui.line5.text()
        sub6=self.ui.line6.text()
        l=[sub1,sub2,sub3,sub4,sub5,sub6]
        file=open('mainCode/textfiles/subjects.txt','w')
        for i in range(6):
            file.write(l[i]+'\n')
        file.close()
        qApp.quit()




app=QApplication(sys.argv)
win=save_attd()
win.setWindowTitle('Subjects')
win.show()
sys.exit(app.exec_())