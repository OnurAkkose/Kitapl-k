from PyQt5.QtWidgets import*
from PyQt5.QtGui import QIcon
from sonekle import Ui_Form
from PyQt5.uic import loadUi
from tkinter import messagebox
import sqlite3

class ekleSayfası(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)





        self.ui.pshekle.clicked.connect(self.ekledb)
    def ekledb(self):
        con = sqlite3.connect("kitapdb.db")
        cursor = con.cursor()
        kitap=self.ui.txtisim.text()
        cursor.execute("Insert into Kitaplar(KitapAdı)  Values(?)",(kitap,))
        con.commit()
        messagebox.showinfo("Tebrikler", "Kitap Eklendi")






