from PyQt5.QtWidgets import*
from PyQt5.QtGui import QIcon
from tasarım1 import Ui_Form
from ekleSayfa import ekleSayfası
from alıntıSayfa import alıntıSayfası
from kitapEkle import yeniKitaplar
import sqlite3






class Uygulama(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui=Ui_Form()
        self.ui.setupUi(self)
        con = sqlite3.connect("kitapdb.db")
        cursor = con.cursor()







        self.setWindowIcon(QIcon("icons/unnamed.ico"))

        self.ui.btnekle.setIcon(QIcon("icons/unnamed.ico"))
        self.ui.btnalintiekle.setIcon(QIcon("icons/note-512.ico"))
        self.ui.btnoku.setIcon(QIcon("icons/txt-icon.ico"))
        self.statusBar().setSizeGripEnabled(False)

        self.ui.lblsayi.setStyleSheet("font: 75 25pt")

        #clicked eventler
        self.ui.btnoku.clicked.connect(self.ekleOku)
        self.kitapEkle=yeniKitaplar()
        self.ui.btnalintiekle.clicked.connect(self.ekleAlinti)
        self.alıntıSayfa=alıntıSayfası()

        self.ui.btnekle.clicked.connect(self.acEkle)

        self.ekleSayfa=ekleSayfası()
        #self.ui.btnalintiekle.clicked.connect(self.acAlıntı)

        #self.alıntıSayfa=alıntıSayfası()




        cursor.execute("Select Alıntı From Alıntılar")
        data=cursor.fetchall()
        for i in data:
            for k in i:
                self.ui.listWidget_2.addItem(k)



        #cursor.execute("select seq from sqlite_sequence where name='Kitaplar';")
        cursor.execute(" Select count(*) as Satır_Sayısı  from Kitaplar ")
        data=cursor.fetchall()

        for i in data:
            for k in i:
                #print(k)
                self.ui.lblsayi.setText(str(k))



        cursor.execute("Select KitapAdı From Kitaplar")
        data=cursor.fetchall()

        for i in data:
            for k in i:
                self.ui.listWidget.addItem(k)


    def acEkle(self):
         self.ekleSayfa.show()
    def ekleAlinti(self):
        self.alıntıSayfa.show()
    def ekleOku(self):
        self.kitapEkle.show()





app=QApplication([])
pencere=Uygulama()
pencere.show()
app.exec_()

