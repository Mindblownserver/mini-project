from PyQt5.QtWidgets import QWidget,QTableWidget, QTableWidgetItem
from PyQt5.uic import loadUi
import os
class AfficherNatPage(QWidget):
    def __init__(self,personnes):
        super().__init__()
        path = os.path.dirname(__file__) + "/"
        ui_file = path+"nat.ui"
        self.nat=set()
        loadUi(ui_file, self)
        self.loadData(personnes)
        self.listeOp.itemClicked.connect(lambda item: self.showData(self.persNat(item.text(),personnes)))
        self.returnBtn.clicked.connect(self.goHome)
        self.show()

    def goHome(self):
        self.parent().setCurrentIndex(0)
    def loadData(self,personnes):
        self.cr ={personne["Nationalite"] for personne in personnes}
        self.listeOp.addItems(list(self.cr))
    def persNat(self,nat,personnes):
        personneFiltre=list()
        for personne in personnes:
            if personne["Nationalite"] == nat:
                personneFiltre.append(personne)
        return personneFiltre
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
    