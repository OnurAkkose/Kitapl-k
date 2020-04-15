from PyQt5.QtWidgets import*
from PyQt5.QtGui import QIcon
from tümalintilar import Ui_Form
from PyQt5.uic import loadUi
from tkinter import messagebox

import sqlite3

class alintilar(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.getir)
    def getir(self):
        con = sqlite3.connect("kitapdb.db")
        cursor = con.cursor()
        isim=self.ui.lineEdit.text()
        cursor.execute("Select ID From Kitaplar WHERE KitapAdı='%s'"%isim)
        id=cursor.fetchall()
        cursor.execute("Select Alıntı From Alıntılar WHERE ID='%d'"%id[0])
        veri=cursor.fetchall()
        for i in veri:
            for k in i:
                self.ui.textEdit.append(k)
