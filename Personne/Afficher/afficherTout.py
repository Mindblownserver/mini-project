import csv
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QWidget
import os
# Initialisation de l'application
class AfficherWindow(QWidget):
    def __init__(self,personnes,message="",critere="",st=""):
        super().__init__()
        self.path = os.path.dirname(__file__) + "/"
        ui_file = self.path+"affichageUi.ui"
        loadUi(ui_file, self)
        self.cr = critere
        self.afficheMode(message)
        self.showData(personnes,st)
        # Recherche listener
        #self.msg.textChanged.connect(lambda x: print(x))
        self.rechercheBtn.clicked.connect(lambda: self.showData(self.rechercheClassic(personnes),st))
        self.returnBtn.clicked.connect(self.goHome)
        self.show()
    
    def showData(self, personnes,st):
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setRowCount(self.lenPersonne(personnes,st))
        cp=0
        for row, personne in enumerate(personnes):
            if(st in personne["Decede"]):
                print(row,cp,sep="\t")
                row+=cp
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
            else:
                cp-=1
    
    def goHome(self):
        self.parent().setCurrentIndex(0)

    def afficheMode(self,msg):
        if(self.cr=="Tout"):
            self.critere.hide()
        elif(self.cr=="indi"):
            self.msgTel.setMaximum(99)
            self.msg.hide()
            self.cr="Tel"
        elif(self.cr == "Tel"):
            self.msg.hide()
        else:
            self.msgTel.hide()
        self.text.setText(msg)
    
    def lenPersonne(self,personnes,st):
        if st=="": return len(personnes)
        return (len([0 for personne in personnes if personne["Decede"] == st]))
    
    def rechercheClassic(self,personnes):
        text = self.msg.text() if(self.cr!="Tel") else str(self.msgTel.value())
        personneCherche= list(dict())
        if(text=="0"):return personnes
        for personne in personnes:
            if (text.lower() in personne[self.cr].lower()):
                personneCherche.append(personne)          
        return personneCherche
        