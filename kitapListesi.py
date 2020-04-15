from PyQt5.QtWidgets import*
from PyQt5.QtGui import QIcon
from kitaplist import Ui_Form
from PyQt5.uic import loadUi
from tkinter import messagebox

import sqlite3

class listele(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        con=sqlite3.connect("kitapdb.db")
        cursor=con.cursor()
        cursor.execute("Select *From Okunacaklar")
        veri=cursor.fetchall()
        for i in veri:
            for k in i:
                self.ui.listWidget.addItem(k)

