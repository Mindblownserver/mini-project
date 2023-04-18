from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QModelIndex
#from assets.widgets.messageBox import MessageBox
import os

class SupprimerPage(QWidget):
    def __init__(self,personnes):
        super().__init__()
        path = os.path.dirname(__file__) + "/"
        ui_file = path+"supprimer.ui"
        self.lCIN=list()
        loadUi(ui_file, self)
        self.infoPers.hide()
        self.showData(personnes)
        self.list.itemDoubleClicked.connect(lambda item: self.showPersonne(item,personnes))
        self.suppBtn.clicked.connect(lambda: self.deletePersonne(personnes))
        self.returnBtn.clicked.connect(self.goHome)
        self.show()
    
    def goHome(self):
        self.parent().setCurrentIndex(0)

    def showData(self,personnes):
        for personne in personnes:
            self.list.addItem(f"{personne['Prenom']} {personne['Nom']}")
            self.lCIN.append(personne["CIN"])
    def showPersonne(self,item,personnes):
        index = self.list.indexFromItem(item).row()
        personne = personnes[index]
        # Insert data to right widget
        self.nom.setText(f"{personne['Prenom']} {personne['Nom']}")
        self.CIN.setText(personne["CIN"])
        self.age.setText(personne["Age"])
        self.adr.setText(personne["Adresse"])
        self.nat.setText(personne["Nationalite"])
        self.tel.setText(personne["Tel"])
        self.DInfect.setText(f"{personne['Jour']}/{personne['Mois']}/{personne['Annee']}")
        self.dead.setText(personne["Decede"])

        self.infoPers.show()
    def deletePersonne(self,personnes):
        cin = self.CIN.text()
        index = self.lCIN.index(cin)
        self.lCIN.pop(index)
        personnes.pop(index)
        self.list.removeItemWidget(self.list.itemFromIndex(index)) # problem here
        self.goHome()