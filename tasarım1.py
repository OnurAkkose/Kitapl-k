# -*- coding: utf-8 -*-


#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(1000, 777)
        Form.setMaximumSize(QtCore.QSize(1000, 1000))
        Form.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("unnamed.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("#Form{\n"
"border-image: url(:/newPrefix/book.jpg);\n"
"}")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 480, 301, 41))
        self.label_2.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 39, 0);")
        self.label_2.setObjectName("label_2")
        self.lblsayi = QtWidgets.QLabel(Form)
        self.lblsayi.setGeometry(QtCore.QRect(370, 480, 111, 41))
        self.lblsayi.setStyleSheet("color:rgb(170, 0, 0);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lblsayi.setText("")
        self.lblsayi.setObjectName("lblsayi")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 570, 301, 41))
        self.label_3.setStyleSheet("color: rgb(0, 39, 0);\n"

"font: 16pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(190, 50, 551, 201))
        self.groupBox.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(0, 0, 0);")
        self.groupBox.setObjectName("groupBox")
        self.btnekle = QtWidgets.QPushButton(self.groupBox)
        self.btnekle.setGeometry(QtCore.QRect(120, 30, 311, 41))
        self.btnekle.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"color: rgb(255, 255, 127);")
        self.btnekle.setIcon(icon)
        self.btnekle.setObjectName("btnekle")
        self.btnalintiekle = QtWidgets.QPushButton(self.groupBox)
        self.btnalintiekle.setGeometry(QtCore.QRect(120, 90, 311, 41))
        self.btnalintiekle.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"color: rgb(255, 255, 127);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("note-512.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnalintiekle.setIcon(icon1)
        self.btnalintiekle.setObjectName("btnalintiekle")
        self.btnoku = QtWidgets.QPushButton(self.groupBox)
        self.btnoku.setGeometry(QtCore.QRect(120, 150, 311, 41))
        self.btnoku.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"color: rgb(255, 255, 127);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("txt-icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnoku.setIcon(icon2)
        self.btnoku.setObjectName("btnoku")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(830, 310, 121, 41))
        self.label_4.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 39, 0);")
        self.label_4.setObjectName("label_4")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(360, 580, 256, 192))
        self.listWidget.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 170, 255);\n"
"color: rgb(0, 0, 0);")
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(Form)
        self.listWidget_2.setGeometry(QtCore.QRect(740, 390, 256, 192))
        self.listWidget_2.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 170, 255);\n"
"color: rgb(0, 0, 0);")
        self.listWidget_2.setObjectName("listWidget_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kitap Takip"))
        self.label_2.setText(_translate("Form", "Okuduğun Kitap Sayısı:"))
        self.label_3.setText(_translate("Form", "Son Okuduğun Kitaplar:"))
        self.groupBox.setTitle(_translate("Form", "Ekle"))
        self.btnekle.setText(_translate("Form", "Yeni Kitap Ekle"))
        self.btnalintiekle.setText(_translate("Form", "Yeni Alıntı Ekle"))
        self.btnoku.setText(_translate("Form", "Okumak İstediğim Kitaplar"))
        self.label_4.setText(_translate("Form", "Son Alıntı"))

import image_rc
