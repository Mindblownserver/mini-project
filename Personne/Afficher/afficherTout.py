import csv
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QWidget
import os
# fetch data


# Initialisation de l'application
class AfficherWindow(QWidget):
    def __init__(self,critere=""):
        super().__init__()
        self.path = os.path.dirname(__file__) + "/"
        self.personnes = list(dict())
        ui_file = self.path+"affichageUi.ui"
        loadUi(ui_file, self)

        self.afficheMode(critere)
        self.getDataFromFile()
        self.showData(self.personnes)
        # Recherche listener
        #self.msg.textChanged.connect(lambda x: print(x))


        self.returnBtn.clicked.connect(self.goHome)
        self.show()
    def goHome(self):
        self.parent().setCurrentIndex(0)

    def afficheMode(self,msg):
        if(msg=="Tout"):
            self.critere.hide()
        self.text.setText(msg)

    def getDataFromFile(self):
        with open(self.path+"personnes.csv") as file:
            reader = csv.reader(file, delimiter=",")
            for i, row in enumerate(reader):
                if i != 0:
                    self.personnes.append({
                        "CIN": row[0],
                        "Nom": row[1],
                        "Prenom": row[2],
                        "Tel": row[3],
                        "Nationalite": row[4],
                        "Age": row[5],
                        "Jour": row[6],
                        "Mois": row[7],
                        "Annee": row[8],
                        "Decede": row[9],
                    })

    def showData(self, personnes):
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setRowCount(len(personnes))
        for row, personne in enumerate(personnes):
            self.table.setItem(row, 0, QTableWidgetItem(personne["CIN"]))
            self.table.setItem(row, 1, QTableWidgetItem(personne["Nom"]))
            self.table.setItem(row, 2, QTableWidgetItem(personne["Prenom"]))
            self.table.setItem(row, 3, QTableWidgetItem(personne["Tel"]))
            self.table.setItem(
                row, 4, QTableWidgetItem(personne["Nationalite"]))
            self.table.setItem(row, 5, QTableWidgetItem(personne["Age"]))
            self.table.setItem(row, 6, QTableWidgetItem(personne["Jour"]))
            self.table.setItem(row, 7, QTableWidgetItem(personne["Mois"]))
            self.table.setItem(row, 8, QTableWidgetItem(personne["Annee"]))
            self.table.setItem(row, 9, QTableWidgetItem(personne["Decede"]))