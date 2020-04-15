# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Onur\Desktop\designers\sonekle.ui'
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
        Form.setStyleSheet("#Form{\n"
"border-image: url(:/newPrefix/library.jpg);\n"
"}")
        self.txtisim = QtWidgets.QLineEdit(Form)
        self.txtisim.setGeometry(QtCore.QRect(40, 120, 401, 51))
        self.txtisim.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.txtisim.setObjectName("txtisim")
        self.pshekle = QtWidgets.QPushButton(Form)
        self.pshekle.setGeometry(QtCore.QRect(260, 260, 191, 51))
        self.pshekle.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 85, 0);\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/plus-one.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pshekle.setIcon(icon1)
        self.pshekle.setObjectName("pshekle")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Yeni Kitap"))
        self.txtisim.setPlaceholderText(_translate("Form", "Kitap İsmi"))
        self.pshekle.setText(_translate("Form", "EKLE"))

import image2_rc
import image3_rc
