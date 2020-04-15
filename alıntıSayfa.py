from PyQt5.QtWidgets import*
from PyQt5.QtGui import QIcon
from alintitasarim import Ui_Form
from PyQt5.uic import loadUi
from tkinter import messagebox
from sayfaAlintilar import alintilar

import sqlite3

class alıntıSayfası(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pshekle.clicked.connect(self.alintiEkle)
        self.ui.pshalintilar.clicked.connect(self.alintilarim)
        self.sayfaAlintilar=alintilar()

    def alintilarim(self):
        self.sayfaAlintilar.show()

    def alintiEkle(self):
        con = sqlite3.connect("kitapdb.db")
        cursor = con.cursor()
        isim=self.ui.txthangisi.text()
        alinti=self.ui.txtalinti.text()
        cursor.execute("Select ID From Kitaplar Where KitapAdı='%s'"%(isim))
        id=cursor.fetchall()
        strings = [str(integer) for integer in id[0]]
        a_string = "".join(strings)
        an_integer = int(a_string)

        cursor.execute("Insert into Alıntılar Values(?,?)",(an_integer,alinti))
        con.commit()



