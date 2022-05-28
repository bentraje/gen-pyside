import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QTextEdit,QAction,QFileDialog,qApp,QFontDialog,QMessageBox
from PyQt5.Qt import QFont,QIcon
class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit=QTextEdit()
        self.setCentralWidget(self.textEdit)
        menubar=self.menuBar()
        self.statusbar=self.statusBar()
        fileac=QAction('Open',self)
        fileac.setShortcut('Ctrl+O')
        fileac.setStatusTip('Open file')
        fileac.setIcon(QIcon('mainCode/TextEditorImages/open.png'))
        fileac.triggered.connect(self.fileDialog)

        new_act=QAction('New',self)
        new_act.setIcon(QIcon('mainCode/TextEditorImages/o_new.png'))
        new_act.setStatusTip('Open new file')
        new_act.setShortcut('Ctrl+N')
        new_act.triggered.connect(self.newDialog)

        save_act=QAction('Save',self)
        save_act.setIcon(QIcon('mainCode/TextEditorImages/o_save.png'))
        save_act.setStatusTip('Save file')
        save_act.setShortcut('Ctrl+S')
        save_act.triggered.connect(self.saveDialog)

        exit_act=QAction('Exit',self)
        exit_act.setIcon(QIcon('mainCode/TextEditorImages/exit.png'))
        exit_act.setShortcut('Ctr+Q')
        exit_act.setStatusTip('Exit')
        exit_act.triggered.connect(self.exit_fn)

        filemenu=menubar.addMenu('File')
        filemenu.addAction(fileac)
        filemenu.addAction(new_act)
        filemenu.addAction(save_act)
        filemenu.addAction(exit_act)

        copy_act=QAction('Copy',self)
        copy_act.setStatusTip('copy text')
        copy_act.setShortcut('Ctrl+C')
        copy_act.triggered.connect(self.textEdit.copy)

        paste_act=QAction('Paste',self)
        paste_act.setShortcut('Ctrl+V')
        paste_act.setStatusTip('Paste text')
        paste_act.triggered.connect(self.textEdit.paste)

        cut_act=QAction('Cut',self)
        cut_act.setStatusTip('Cut text')
        cut_act.setShortcut('Ctrl+X')
        cut_act.triggered.connect(self.textEdit.cut)

        delete_act=QAction('Delete',self)
        delete_act.setIcon(QIcon('mainCode/TextEditorImages/delete.jpg'))
        delete_act.setShortcut('del')
        delete_act.setStatusTip('Delete text')
        delete_act.triggered.connect(self.textEdit.clear)

        undo_act=QAction('Undo',self)
        undo_act.setStatusTip('Undo')
        undo_act.setShortcut('Ctrl+Z')
        undo_act.triggered.connect(self.textEdit.undo)

        redo_act=QAction('Redo',self)
        redo_act.setShortcut('Ctrl+shift+Z')
        redo_act.setStatusTip('Redo')
        redo_act.triggered.connect(self.textEdit.redo)

        font_act=QAction('Font',self)
        font_act.setStatusTip('Change Font')
        font_act.setIcon(QIcon('mainCode/TextEditorImages/o_font.png'))
        font_act.triggered.connect(self.fontDialog)

        bold_act=QAction('Bold',self)
        bold_act.setStatusTip('Bold text')
        bold_act.setIcon(QIcon('mainCode/TextEditorImages/o_bold.png'))
        bold_act.setShortcut('Ctrl+B')
        bold_act.triggered.connect(self.font_bold)

        italic_act=QAction('Italic',self)
        italic_act.setStatusTip('Italic font')
        italic_act.setShortcut('Ctrl+I')
        italic_act.setIcon(QIcon('mainCode/TextEditorImages/o_italic.png'))
        italic_act.triggered.connect(self.italic)

        view_act=QAction('View statusbar',self)
        view_act.setCheckable(True)
        view_act.triggered.connect(self.status)



        editmenu=menubar.addMenu('Edit')
        editmenu.addAction(copy_act)
        editmenu.addAction(paste_act)
        editmenu.addAction(cut_act)
        editmenu.addAction(delete_act)
        editmenu.addAction(undo_act)
        editmenu.addAction(redo_act)

        formatMenu=menubar.addMenu('Format')
        formatMenu.addAction(font_act)
        formatMenu.addAction(bold_act)
        formatMenu.addAction(italic_act)

        viewmenu=menubar.addMenu('View')
        viewmenu.addAction(view_act)

        self.exit_toolbar=self.addToolBar('Exit')
        self.save_toolbar=self.addToolBar('Save')
        self.file_toolbar=self.addToolBar('File')
        self.delete_toolbar=self.addToolBar('Delete')
        self.font_toolbar=self.addToolBar('Font')
        self.bold_toolbar=self.addToolBar('Bold')
        self.italic_toolbar=self.addToolBar('Italic')
        self.new_toolbar=self.addToolBar('New')

        self.new_toolbar.addAction(new_act)
        self.save_toolbar.addAction(save_act)
        self.file_toolbar.addAction(fileac)
        self.delete_toolbar.addAction(delete_act)
        self.font_toolbar.addAction(font_act)
        self.bold_toolbar.addAction(bold_act)
        self.italic_toolbar.addAction(italic_act)


        self.setGeometry(100,100,800,400)
        self.setWindowTitle('Text Editor')
        self.show()

    def fileDialog(self):
        text=QFileDialog.getOpenFileName(self,'open','/new')
        if text[0] is None:
            return


        if text[0]:
            f=open(text[0],'r')
            with f:
             data=f.read()
             self.textEdit.setText(data)
    def newDialog(self):
        self.textEdit.clear()
    def saveDialog(self):
        name= QFileDialog.getSaveFileName(self, "Save file",'', "Text documents (*.txt);;All files (*.*)")
        try:
           f=open(name[0],'w')
           with f:
             data=self.textEdit.toPlainText()
             f.write(data)
           f.close()

        except Exception as e:
           self.exception_dialog(str(e))

    def exit_fn(self):
        qApp.quit()

    def fontDialog(self):
        text,ok= QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(text)
    def font_bold(self):
        self.textEdit.setFontWeight(QFont.Bold)

    def italic(self):
        self.textEdit.setFontItalic(True)
    def status(self,state):
        if state:
            self.statusbar.hide()
        else:
            self.statusbar.show()

    def exception_dialog(self,s):
        QMessageBox.warning(self,'warning',s,QMessageBox.Ok)
        return

app=QApplication(sys.argv)
win=window()
sys.exit(app.exec_())
