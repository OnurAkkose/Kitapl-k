from PyQt5.QtWidgets import*
from PyQt5.QtGui import QIcon
from kitapekletasarim import Ui_Form
from PyQt5.uic import loadUi
from tkinter import messagebox
from kitapListesi import listele

import sqlite3

class yeniKitaplar(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pshekle.clicked.connect(self.ekleKitap)
        self.ui.pshhepsi.clicked.connect(self.sirala)
        self.kitapListesi=listele()
    def sirala(self):
        self.kitapListesi.show()


    def ekleKitap(self):
        con=sqlite3.connect("kitapdb.db")
        cursor=con.cursor()
        isim=self.ui.txtadi.text()
        cursor.execute("Insert into Okunacaklar Values(?)",(isim,))
        con.commit()
        messagebox.showinfo("Tebrikler", "Kitap Eklendi")