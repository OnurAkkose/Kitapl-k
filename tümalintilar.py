# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Onur\Desktop\designers\tümalintilar.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 600)
        Form.setMaximumSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/background/unnamed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("#Form{\n"
"border-image: url(:/newPrefix/note-icon.png);\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 90, 131, 31))
        self.label.setStyleSheet("font: 75 14pt \"MS Serif\";\n"
"background-color: rgb(170, 255, 255);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(230, 90, 271, 31))
        self.lineEdit.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(320, 190, 171, 41))
        self.pushButton.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 0);")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(60, 310, 481, 211))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Alıntılarım"))
        self.label.setText(_translate("Form", "Kitap Adı:"))
        self.pushButton.setText(_translate("Form", "Alıntıları Gör"))

import image4_rc
