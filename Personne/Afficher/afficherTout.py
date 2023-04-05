import csv
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QWidget
import os
# fetch data


# Initialisation de l'application
class AfficherWindow(QWidget):
    def __init__(self,message,critere):
        super().__init__()
        self.path = os.path.dirname(__file__) + "/"
        self.personnes = list(dict())
        ui_file = self.path+"affichageUi.ui"
        loadUi(ui_file, self)

        self.afficheMode(message,critere)
        self.getDataFromFile(critere)
        self.showData(self.personnes)
        # Recherche listener
        #self.msg.textChanged.connect(lambda x: print(x))
        self.rechercheBtn.clicked.connect(lambda: self.showData(self.recherche(critere=critere)))
        self.returnBtn.clicked.connect(self.goHome)
        self.show()
    def getDataFromFile(self,critere):
        with open(os.getcwd()+"/assets/data/personnes.csv") as file:
            reader = csv.reader(file, delimiter=",")
            for i, row in enumerate(reader):
                if i != 0:
                    if(critere[0].isdigit() and row[9]!=critere[0]):
                        continue
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
            self.table.setItem(row, 4, QTableWidgetItem(personne["Nationalite"]))
            self.table.setItem(row, 5, QTableWidgetItem(personne["Age"]))
            self.table.setItem(row, 6, QTableWidgetItem(personne["Jour"]))
            self.table.setItem(row, 7, QTableWidgetItem(personne["Mois"]))
            self.table.setItem(row, 8, QTableWidgetItem(personne["Annee"]))
            self.table.setItem(row, 9, QTableWidgetItem(personne["Decede"]))
    
    def goHome(self):
        self.parent().setCurrentIndex(0)

    def afficheMode(self,msg,cr):
        if(cr=="Tout"):
            self.critere.hide()
        self.text.setText(msg)

    def recherche(self,critere):
        text = self.msg.text()
        personneCherche= list(dict())
        for personne in self.personnes:
            if (text.lower() in personne[critere].lower()):
                personneCherche.append(personne)          
        return personneCherche
        