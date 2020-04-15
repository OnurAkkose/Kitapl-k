# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Onur\Desktop\designers\kitapekletasarim.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 400)
        Form.setMaximumSize(QtCore.QSize(500, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/background/unnamed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.txtadi = QtWidgets.QLineEdit(Form)
        self.txtadi.setGeometry(QtCore.QRect(90, 70, 311, 41))
        self.txtadi.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 255, 255);")
        self.txtadi.setObjectName("txtadi")
        self.pshekle = QtWidgets.QPushButton(Form)
        self.pshekle.setGeometry(QtCore.QRect(300, 210, 151, 41))
        self.pshekle.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 0);")
        self.pshekle.setObjectName("pshekle")
        self.pshhepsi = QtWidgets.QPushButton(Form)
        self.pshhepsi.setGeometry(QtCore.QRect(30, 210, 201, 41))
        self.pshhepsi.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);")
        self.pshhepsi.setObjectName("pshhepsi")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Not"))
        self.txtadi.setPlaceholderText(_translate("Form", "Kitap Adı"))
        self.pshekle.setText(_translate("Form", "Ekle"))
        self.pshhepsi.setText(_translate("Form", "Okuyacağım Kitaplar"))

import image4_rc
