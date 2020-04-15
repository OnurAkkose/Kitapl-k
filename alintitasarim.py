# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Onur\Desktop\designers\alintitasarim.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 450)
        Form.setMaximumSize(QtCore.QSize(500, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/background/unnamed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("#Form{\n"
"border-image: url(:/newPrefix/note-icon.png);\n"
"}")
        self.txthangisi = QtWidgets.QLineEdit(Form)
        self.txthangisi.setGeometry(QtCore.QRect(42, 71, 341, 41))
        self.txthangisi.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.txthangisi.setObjectName("txthangisi")
        self.pshekle = QtWidgets.QPushButton(Form)
        self.pshekle.setGeometry(QtCore.QRect(310, 370, 161, 51))
        self.pshekle.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 0);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/plus-one.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pshekle.setIcon(icon1)
        self.pshekle.setObjectName("pshekle")
        self.pshalintilar = QtWidgets.QPushButton(Form)
        self.pshalintilar.setGeometry(QtCore.QRect(30, 370, 161, 51))
        self.pshalintilar.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.pshalintilar.setObjectName("pshalintilar")
        self.txtalinti = QtWidgets.QLineEdit(Form)
        self.txtalinti.setGeometry(QtCore.QRect(40, 190, 341, 41))
        self.txtalinti.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.txtalinti.setObjectName("txtalinti")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Alıntı"))
        self.txthangisi.setPlaceholderText(_translate("Form", "Hangi Kitap"))
        self.pshekle.setText(_translate("Form", "Ekle"))
        self.pshalintilar.setText(_translate("Form", "Alıntılarım"))
        self.txtalinti.setPlaceholderText(_translate("Form", "Alıntı"))

import image4_rc
