import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QInputDialog,QCheckBox
from PyQt5 import uic

qtCreator='mainCode/UiFiles/cal.ui'
ui_mainwindow,QtBaseClass=uic.loadUiType(qtCreator)

i=0
j=0

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.ui=ui_mainwindow()
        self.ui.setupUi(self)
        self.ui.progress.setValue(0)
        self.ui.cal.clicked.connect(self.selectdate)
        self.setWindowTitle('UI')
        self.ui.edit.clicked.connect(self.add_todo)

    def selectdate(self):
        date=self.ui.cal.selectedDate().toString()
        print(date)
        print(type(date))
        file=open(date,'w')
        file.write('file opened')
        file.close()

    def add_todo(self):
        text,ok=QInputDialog.getText(self,'Add to do','Task')
        global name
        if ok:
          name=QCheckBox()
          name.setEnabled(True)
          name.setText(text)
          self.countcheck()
          self.ui.fLayout.addWidget(name)
        name.stateChanged.connect(self.taskCheck)

    def countcheck(self):
        global i
        i+=1
        print(i)
    def taskCheck(self):
        global j
        global name
        j+=1
        print(j)
        self.progressBar()

    def progressBar(self):
        global i
        global j
        if i!=0 and j!=0:
         self.ui.progress.setValue((100/i)*j)

app=QApplication(sys.argv)
widget=Window()
widget.setWindowTitle('Calender')
widget.show()
sys.exit(app.exec_())