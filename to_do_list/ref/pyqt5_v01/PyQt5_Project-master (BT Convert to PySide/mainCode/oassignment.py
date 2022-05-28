import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QInputDialog,QCheckBox
from PyQt5 import uic

qtCreator='mainCode/UiFiles/d_assignment.ui'
Ui_MainWindow,QtBaseClass=uic.loadUiType(qtCreator)

class widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        sub1_open=open('mainCode/textfiles/sub1.txt','r')
        sub2_open = open('mainCode/textfiles/sub2.txt', 'r')
        sub3_open = open('mainCode/textfiles/sub3.txt', 'r')
        sub4_open = open('mainCode/textfiles/sub4.txt', 'r')
        sub5_open = open('mainCode/textfiles/sub5.txt', 'r')
        sub6_open = open('mainCode/textfiles/sub6.txt', 'r')

        sub_list=[sub1_open,sub2_open,sub3_open,sub4_open,sub5_open,sub6_open]


        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        subject=open('mainCode/textfiles/subjects.txt','r')
        form_list=[self.ui.formL_1,self.ui.formL_2,self.ui.formL_3,self.ui.formL_4,self.ui.formL_5,self.ui.formL_6]
        i=0
        for line in subject:
            while i<6:
                label=QLabel()
                label.setText(line)
                form_list[i].addWidget(label)
                i+=1
        i=0
        j=1
        line_count=0
        for sub in sub_list:
            for line in sub:
                if line_count!=0:
                  if j%2!=0:
                    open_checkbox = QLabel()
                    open_checkbox.setText(line)
                    form_list[i].addWidget(open_checkbox)
                    j+=1
                  else:
                    open_checkbox.setToolTip(line)
                    j+=1
                line_count+=1
            i+=1
            j=1
            line_count=0
        self.ui.add_1.clicked.connect(self.add_assignment)
        self.ui.add_2.clicked.connect(self.add_assignment)
        self.ui.add_3.clicked.connect(self.add_assignment)
        self.ui.add_4.clicked.connect(self.add_assignment)
        self.ui.add_5.clicked.connect(self.add_assignment)
        self.ui.add_6.clicked.connect(self.add_assignment)

    def add_assignment(self):
        text,ok=QInputDialog.getText(self,'Assignment','assignment')
        date,ok2=QInputDialog.getText(self,'Enter date of submission','Format: dd/mm/yyyy')
        if ok and ok2:
            label=QLabel()
            label.setText(text)
            label.setToolTip('Submission date: '+date + '\n')
        if self.sender()==self.ui.add_1:
            self.ui.formL_1.addWidget(label)
            sub1 = open('mainCode/textfiles/sub1.txt', 'a')
            sub1.write(text+'\n')
            sub1.write('Submission date: '+date + '\n')
            sub1.close()

        if self.sender()==self.ui.add_2:
            sub2 = open('mainCode/textfiles/sub2.txt', 'a')
            self.ui.formL_2.addWidget(label)
            sub2.write(text+'\n')
            sub2.write('Submission date: '+date + '\n')
            sub2.close()

        if self.sender()==self.ui.add_3:
            sub3 = open('mainCode/textfiles/sub3.txt', 'a')
            self.ui.formL_3.addWidget(label)
            sub3.write(text+'\n')
            sub3.write('Submission date: '+date + '\n')
            sub3.close()

        if self.sender()==self.ui.add_4:
            self.ui.formL_4.addWidget(label)
            sub4 = open('mainCode/textfiles/sub4.txt', 'a')
            sub4.write(text+'\n')
            sub4.write('Submission date: '+date + '\n')
            sub4.close()

        if self.sender()==self.ui.add_5:
            sub5 = open('mainCode/textfiles/sub5.txt', 'a')
            self.ui.formL_5.addWidget(label)
            sub5.write(text+'\n')
            sub5.write('Submission date: '+date + '\n')
            sub5.close()

        if self.sender()==self.ui.add_6:
            sub6 = open('mainCode/textfiles/sub6.txt', 'a')
            self.ui.formL_6.addWidget(label)
            sub6.write(text+'\n')
            sub6.write('Submission date: '+date + '\n')
            sub6.close()




app=QApplication(sys.argv)
win=widget()
win.show()
sys.exit(app.exec_())
