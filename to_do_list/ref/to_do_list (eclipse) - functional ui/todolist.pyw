import sys
import os
from PyQt5 import QtWidgets, QtCore
from todo2 import Ui_MainWindow


class Todo(QtWidgets.QMainWindow, Ui_MainWindow):
    i = 0
    waitforadd = True
    cwd = os.getcwd()

    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        self.addbtn.clicked.connect(self.addtodo)
        self.clearallbtn.clicked.connect(self.clearall)
        self.deletebtn.clicked.connect(self.deleteitem)
        self.savebtn.clicked.connect(self.savefile)
        self.loadbtn.clicked.connect(self.loadfile)

    def addtodo(self):
        text = self.addlist.text()

        if text != "":
            self.todolist.addItem(text)
            self.addlist.clear()

    def clearall(self):
        self.todolist.clear()
        self.waitforadd = True

    def deleteitem(self):
        self.todolist.takeItem(self.todolist.currentRow())

    def savefile(self):
        with open("todo.txt", 'w', encoding='UTF-8') as thefile:
            for i in range(self.todolist.count()):
                thefile.write(str(self.todolist.item(i).text())+"\n")
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(u"提示")
        msg.setInformativeText(u"存檔成功！")
        msg.exec_()

    def loadfile(self):
        self.todolist.clear()
        try:
            myfile = QtWidgets.QFileDialog.getOpenFileName(
                self, "Open file", self.cwd, "Text Files (*.txt)")
            with open(myfile[0], "r", encoding='UTF-8') as thefile:
                for line in thefile.readlines():
                    line = line.strip()
                    self.todolist.addItem(line)

        except FileNotFoundError:
            pass

    def keyPressEvent(self, qKeyEvent):
        print(qKeyEvent.key())
        if qKeyEvent.key() == QtCore.Qt.Key_F:
            if (QtWidgets.QApplication.keyboardModifiers() ==
                    QtCore.Qt.ControlModifier):
                self.loadfile()

        if qKeyEvent.key() == QtCore.Qt.Key_S:
            if (QtWidgets.QApplication.keyboardModifiers() ==
                    QtCore.Qt.ControlModifier):
                self.savefile()
                print("存檔成功")

        else:
            super().keyPressEvent(qKeyEvent)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Todo()
    w.show()
    sys.exit(app.exec_())