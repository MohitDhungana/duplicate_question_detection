# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import tensorflow as tf


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkDuplicate = QtWidgets.QPushButton(self.centralwidget)
        self.checkDuplicate.setGeometry(QtCore.QRect(320, 270, 141, 61))
        self.checkDuplicate.setObjectName("checkDuplicate")
        self.question1TextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.question1TextEdit.setGeometry(QtCore.QRect(130, 40, 641, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.question1TextEdit.setFont(font)
        self.question1TextEdit.setObjectName("question1TextEdit")
        self.question2TextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.question2TextEdit.setGeometry(QtCore.QRect(130, 150, 641, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.question2TextEdit.setFont(font)
        self.question2TextEdit.setObjectName("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 101, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 170, 101, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 390, 281, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkDuplicate.setText(_translate("MainWindow", "Check"))
        self.question1TextEdit.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.question1TextEdit.setPlainText(
            _translate("MainWindow", "question 1 text content"))
        self.question2TextEdit.setPlainText(
            _translate("MainWindow", "question 2 text content"))
        self.label.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Question 1:</span></p></body></html>"))
        self.label_2.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Question 2:</span></p></body></html>"))
        self.label_3.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\">output_label</p><p align=\"center\"><br/></p></body></html>"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
