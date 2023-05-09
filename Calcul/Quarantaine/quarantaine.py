from PyQt5.QtWidgets import QWidget,QTableWidget,QTableWidgetItem
from PyQt5.QtCore import QDate
from PyQt5.uic import loadUi
import os
class AffQuaPage(QWidget):
    def __init__(self,personnes):
        super().__init__()
        path = os.path.dirname(__file__) + "/"
        ui_file = path+"quarantaine.ui"
        loadUi(ui_file, self)
        self.showData(self.getPersEnQua(personnes))
        self.returnBtn.clicked.connect(self.goHome)
        self.show()

    def goHome(self):
        self.parent().setCurrentIndex(0)
    
    def getPersEnQua(self,personnes:list):
        res = list()
        #date = QDate(int(personnes[0]["Annee"]),int(personnes[0]["Mois"]),int(personnes[0]["Jour"]),)
        now = QDate().currentDate()
        for personne in personnes:
            date = QDate(int(personne["Annee"]),int(personne["Mois"]),int(personne["Jour"]))
            if ((date.daysTo(now)<=14) and (personne["Decede"]!="1")):
                res.append(personne)
        return res
    
    def showData(self,personnes):
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setRowCount(len(personnes))
        cp=0
        for row, personne in enumerate(personnes):
            self.table.setItem(row, 0, QTableWidgetItem(personne["CIN"]))
            self.table.setItem(row, 1, QTableWidgetItem(personne["Nom"]))
            self.table.setItem(row, 2, QTableWidgetItem(personne["Prenom"]))
            self.table.setItem(row, 3, QTableWidgetItem(personne["Tel"]))
            self.table.setItem(row, 4, QTableWidgetItem(personne["Nationalite"]))
            self.table.setItem(row, 5, QTableWidgetItem(personne["Age"]))
            self.table.setItem(row, 6, QTableWidgetItem(personne["Jour"]))
            self.table.setItem(row, 7, QTableWidgetItem(personne["Mois"]))
            self.table.setItem(row, 8, QTableWidgetItem(personne["Annee"]))
            self.table.setItem(row, 9, QTableWidgetItem(personne["Decede"])) 