import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QCheckBox,QInputDialog,QLabel,QAction
from PyQt5 import uic

qtCreator='mainCode/UiFiles/edit_att.ui'
Ui_Mainwindow,Qt_BaseClass=uic.loadUiType(qtCreator)
i=0
(sub1,sub2,sub3,sub4,sub5,sub6)=(0,0,0,0,0,0)
total_classes=[sub1,sub2,sub3,sub4,sub5,sub6]
(cls1,cls2,cls3,cls4,cls5,cls6)=(0,0,0,0,0,0)
attended_classes=[cls1,cls2,cls3,cls4,cls5,cls6]
k=0
m=0
open_file=open('mainCode/textfiles/attendance.txt','r+')
attendedFile=open('mainCode/textfiles/attendedFile.txt','r+')
for line in open_file:
     if m<6:
         total_classes[m]=int(line)
         m+=1
for mline in attendedFile:
     if k<6:
         attended_classes[k]=int(mline)
         k+=1
print(total_classes)
print(attended_classes)
m=0
k=0

class widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb1=QCheckBox()
        cb2=QCheckBox()
        cb3 = QCheckBox()
        cb4 = QCheckBox()
        cb5 = QCheckBox()
        cb6 = QCheckBox()
        global l
        l=[cb1,cb2,cb3,cb4,cb5,cb6]

        self.ui = Ui_Mainwindow()
        self.ui.setupUi(self)

        c=0
        open_checkbox = open('mainCode/textfiles/subjects.txt', 'r')
        for line in open_checkbox:
            if c < 6:
                l[c].setText(line)
                self.ui.fl.addWidget(l[c])
                c += 1
        open_checkbox.close()
        for n in range(6):
            l[n].setCheckable(False)


        self.save_act = QAction('Save', self)
        self.save_act.setShortcut('Ctrl+S')
        self.save_act.triggered.connect(self.save)

        self.edit_act = QAction('Edit', self)
        self.edit_act.setShortcut('Ctrl+E')
        self.edit_act.triggered.connect(self.edit)

        self.ui.menu.addAction(self.save_act)
        self.ui.menu.addAction(self.edit_act)


        self.ui.edit_btn.clicked.connect(self.edit)
        self.ui.save_btn.clicked.connect(self.save)
        self.ui.add.clicked.connect(self.showLabel)
        cb1.stateChanged.connect(self.attended)
        cb2.stateChanged.connect(self.attended)
        cb3.stateChanged.connect(self.attended)
        cb4.stateChanged.connect(self.attended)
        cb5.stateChanged.connect(self.attended)
        cb6.stateChanged.connect(self.attended)

    def showLabel(self):
        global l
        global attended_classes
        global total_classes

        for m in range(6):
          if attended_classes[m]!=0 and total_classes[m]!=0:
            percentage=(attended_classes[m]/total_classes[m])*100
            label=QLabel()
            label.setText(str(percentage))
            self.ui.LabelVl.addWidget(label)


    def attended(self):
         global l
         global total_classes
         global attended_classes
         global i
         num,ok=QInputDialog.getInt(self,'No. of classes','No. of classes')
         cls_attd,ok=QInputDialog.getInt(self,'No. of classes attended','No. of classes attended')
         if self.sender()==l[0]:
             total_classes[0]+=cls_attd
             attended_classes[0]+=num
         if self.sender()==l[1]:
             total_classes[1]+=1
             attended_classes[1] += num
         if self.sender() == l[2]:
             total_classes[2] += cls_attd
             attended_classes[2] += num
         if self.sender() == l[3]:
             total_classes[3] += cls_attd
             attended_classes[3] += num
         if self.sender() == l[4]:
             total_classes[4] += cls_attd
             attended_classes[4] += num
         if self.sender() == l[5]:
             total_classes[5] += cls_attd
             attended_classes[5] += num

    def save(self):
        global total_classes
        global attended_classes
        print('yay')
        # self.ui.add.setEnabled(False)
        open_file.truncate(0)
        attendedFile.truncate(0)
        for n in range(6):
            open_file.write('{:03d}\n'.format(0))
        for a in range(6):
            attendedFile.write('{:03d}\n'.format(0))
        print(total_classes)
        print(attended_classes)
        open_file.close()
        attendedFile.close()
        file = open('mainCode/attendance.txt', 'w')
        attended_file=open('mainCode/attendedFile.txt','w')
        for n in range(6):
            file.write('{:03d}\n'.format(total_classes[n]))
        for a in range(6):
            attended_file.write('{:03d}\n'.format(attended_classes[a]))
        file.close()
        attended_file.close()



    def edit(self):
        global l
        for n in range(6):
            l[n].setCheckable(True)

app=QApplication(sys.argv)
win=widget()
win.show()
sys.exit(app.exec_())

