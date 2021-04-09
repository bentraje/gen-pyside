import sys
import os
import json
import random

import PySide6
from PySide6 import QtCore
from PySide6.QtCore import Qt, QTimer 
from PySide6.QtWidgets import QApplication, QMainWindow, QSpinBox, QWidget, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QStackedLayout, QRadioButton, QDialog, QDialogButtonBox, QScrollArea, QGroupBox, QFrame
from PySide6 import QtWidgets
from PySide6.QtGui import *

import sqlite3

conn = sqlite3.connect('quiz.db')
cur = conn.cursor()

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("Quiz Application")

        self.setMinimumWidth(500)
        self.setMinimumHeight(500)

        # self.question_list = [
        #
        #     ("水を買っていきます。", ["かって", "つくって", "とって", "あらって"], "かって", "買って"),
        #     ("お先にしつれいします。", ["せん", "ぜん", "ざき", "さき"], "さき", "先"),
        #     ("きのうはゆうはんにぎゅうにくをたべた。", ["牛内", "午内", "牛肉", "午肉"], "午内", "ぎゅうにく"),
        #     ("毎朝、なんじにおきますか。", ["まいにち", "まいとし", "まいげつ", "まいあさ"], "まいあさ", "毎朝"),
        #     ("わたしのこどもははながすきです。", ["了ども", "子ども", "于ども", "予ども"], "子ども", "こども"),
        # ]

        cur.execute('SELECT * FROM vocabulary')
        self.question_list = cur.fetchall()

        (100001, '水を買っていきます。', 'かって', 'つくって', 'とって', 'あらって', 'かって', '買って')

        self.counter = 0


        # Menu Bar

        log_out_action = QAction("&Log Out", self)
        #log_out_action.setShortcut("Ctrl+O")
        #log_out_action.setStatusTip('Log Out')
        log_out_action.triggered.connect(self.logout_cmd)



        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('&File')
        file_menu.addAction(log_out_action)

        # LOG IN LAYOUT

        self.login_layout =  QVBoxLayout()

        login_form_layout = QtWidgets.QFormLayout()
        self.username_edit = QtWidgets.QLineEdit()
        self.password_edit = QtWidgets.QLineEdit()
        self.username_edit.setFixedWidth(120)
        self.password_edit.setFixedWidth(120)
        login_form_layout.addRow(QtWidgets.QLabel("Username"), self.username_edit)
        login_form_layout.addRow(QtWidgets.QLabel("Password"), self.password_edit)


        self.login_btn = QPushButton("Log In")
        self.login_btn.setFixedWidth(120)
        self.login_btn.pressed.connect(self.login_cmd)
        login_form_layout.addWidget(self.login_btn)

        self.login_layout.addLayout(login_form_layout)
        login_form_layout.setFormAlignment(Qt.AlignCenter)

        self.login_widget = QWidget()
        self.login_widget.setLayout(self.login_layout)


        # Main Menu Layout

        self.main_menu_layout =  QVBoxLayout()
        self.logout_btn = QPushButton("Log Out")
        self.logout_btn.setFixedWidth(120)
        self.logout_btn.pressed.connect(self.logout_cmd)
        self.main_menu_layout.addWidget(self.logout_btn)
        self.main_menu_layout.addStretch()

        self.main_menu_widget = QWidget()
        self.main_menu_widget.setLayout(self.main_menu_layout )

        # Quiz Layout

        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.vbox = QVBoxLayout()

        font = QFont()
        font.setFamily('Arial')
        font.setPointSize(18)
        counter = 0
        self.button_list = []
        self.answer_list = []

        for question in self.question_list:
            counter += 1
            self.question_groupbox = QGroupBox()
            self.q_vbox = QVBoxLayout()

            self.quiz_tedit = QTextEdit()

            self.quiz_tedit.setAcceptRichText(True)
            self.quiz_tedit.setReadOnly(True)
            self.quiz_tedit.setFrameStyle(QFrame.NoFrame)
            self.quiz_tedit.setAttribute(Qt.WA_NoSystemBackground, True )
            self.quiz_tedit.setStyleSheet("background-color:transparent;")
            self.quiz_tedit.setFont(font)

            question_proper = question[1]
            split_word = question[7]
            question_sep = question_proper.split("買って")

            if question_sep[0] == "":
                statement = "<u>" + split_word + "</u>" + question_sep[-1]

            elif question_sep[-1] == "":
                statement = question_sep[0] + "<u>" + split_word + "</u>"

            else:
                statement = question_sep[0] + "<u>" + split_word + "</u>" + question_sep[-1]

            statement = "<html>" + statement + "</html>"

            self.quiz_tedit.setText(str(counter) + ") " + statement)

            font = self.quiz_tedit.document().defaultFont()
            fontMetrics = QFontMetrics(font)
            textSize = fontMetrics.size(0, self.quiz_tedit.toPlainText())
            w = textSize.width() + 50
            h = textSize.height() + 10
            self.quiz_tedit.setMinimumSize(w, h)
            self.quiz_tedit.setMaximumSize(w, h)
            self.quiz_tedit.resize(w, h)

            self.q_vbox.addWidget(self.quiz_tedit)
            answer = question[6]

            self.btn_A = QRadioButton(question[2])
            self.btn_B = QRadioButton(question[3])
            self.btn_C = QRadioButton(question[4])
            self.btn_D = QRadioButton(question[5])

            self.button_list.append( [self.btn_A, self.btn_B, self.btn_C, self.btn_D] )
            self.answer_list.append(answer)

            for btn in [self.btn_A, self.btn_B, self.btn_C, self.btn_D]:
                self.q_vbox.addWidget(btn)
                btn.setFont(font)
                btn.setAutoExclusive(True)
            #self.question_groupbox.setFlat(True)
            self.question_groupbox.setLayout(self.q_vbox)
            self.vbox.addWidget(self.question_groupbox)

        self.quiz_submit_btn = QPushButton("Submit")
        self.quiz_submit_btn.clicked.connect(self.submit)
        self.quiz_submit_btn.setFixedWidth(120)

        self.vbox.addWidget(self.quiz_submit_btn)
        self.widget.setLayout(self.vbox)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.quiz_main_hlayout = QHBoxLayout()
        self.quiz_main_hlayout.addWidget(self.scroll)

        self.quiz_widget = QWidget()
        self.quiz_widget.setLayout(self.quiz_main_hlayout)

        # Stack Layout
        self.stack_layout = QStackedLayout()
        self.stack_layout.addWidget(self.login_widget)
        self.stack_layout.addWidget(self.quiz_widget)
        self.stack_layout.setCurrentIndex(0)
        self.stack_layout.setAlignment(QtCore.Qt.AlignCenter)

        widget = QWidget()
        widget.setLayout(self.stack_layout)
        self.setCentralWidget(widget)


    def submit(self):
        for idx, btn_list in enumerate(self.button_list):

            for btn in btn_list:
                if btn.isChecked():
                    if btn.text() == self.answer_list[idx]:
                        print ("You are correct")
                else:
                    pass
            #print ( btn_list[0].isChecked(), btn_list[1].isChecked(), btn_list[2].isChecked(), btn_list[3].isChecked() )
            #print (btn_list)
            print ("=" * 20)

    def quiz_choice(self):

        sender = self.sender()
        key = sender.text()
        print (key)

    def login_cmd(self):

        if self.username_edit.text()=="" or self.password_edit=="":
            QtWidgets.QMessageBox.information(self, 'Message', "Please enter username/password!")
        else:
            cur.execute("SELECT username,password FROM user WHERE username=? AND password=?", (self.username_edit.text(), self.password_edit.text()) )
            record = cur.fetchone()
            if record:
                self.stack_layout.setCurrentIndex(1)
            else:
                QtWidgets.QMessageBox.information(self, 'Message', "Invalid username/password!")

    def logout_cmd(self):
        self.stack_layout.setCurrentIndex(0)

class CustomDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(CustomDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle("Warning")

        #buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        buttons = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(buttons)


        self.buttonBox.accepted.connect(self.accept)
        #self.buttonBox.rejected.connect(self.reject)
        msg_label = QLabel()
        msg_label.setText("Please choose and answer before proceeding")


        self.layout = QVBoxLayout()
        self.layout.addWidget(msg_label)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()