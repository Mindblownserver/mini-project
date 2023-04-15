from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow,QStackedWidget,QWidget
import os
import csv
from Personne.modifer.modifier import ModifierPage
from Personne.Afficher.afficherTout import AfficherWindow
from Personne.Ajouter.ajouter import AjouterPage
from assets.widgets.messageBox import MessageBox
# Initialisation de l'application

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        path = os.path.dirname(__file__) + "/Home/"
        ui_file = path+"home.ui"
        loadUi(ui_file, self)
        


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        path = os.path.dirname(__file__) + "/"
        ui_file = path+"GUI.ui"
        loadUi(ui_file, self)
        self.personnes = list(dict())
        self.stack = QStackedWidget(self)
        self.MiseAJour.setEnabled(False)
        self.Gestion.setEnabled(False)
        self.Calcul.setEnabled(False)
        # Pages
        self.Home = HomePage()
        self.Ajouter = AjouterPage(self.personnes)
        self.stack.addWidget(self.Home)
        self.stack.addWidget(self.Ajouter)
        self.stack.setContentsMargins(0,0,0,0)
        #fdsfsdfdsfsdf
    # Set the central widget to the stacked widget
        self.setCentralWidget(self.stack)
        
        # Mise à jour menu  
        self.actionAjouter.triggered.connect(lambda: self.openPage(self.Ajouter))
        self.actionTel.triggered.connect(lambda: self.openModifier("Téléphone","Tel"))
        self.actionAdresse.triggered.connect(lambda: self.openModifier("Adresse","Adresse"))
        self.actionRPersonne.triggered.connect(self.RPersonne)
        self.actionEPersonne.triggered.connect(self.EPersonne)
        # Recherche & afficher menu
        self.actionAfficher.triggered.connect(lambda :self.openAfficher("Fiche des personnes malades","Tout"))
        self.actionRechercheTel.triggered.connect(lambda :self.openAfficher("Recherche par numéro du Téléphone","Tel"))
        self.actionRechercheInd.triggered.connect(lambda :self.openAfficher("Recherche par indicatif","indi"))
        self.actionRechercheNat.triggered.connect(lambda :self.openAfficher("Recherche par nationalité","Nationalite"))
        self.actionRechercheDecede.triggered.connect(lambda :self.openAfficher("Recherche des personnes décédés", "1Decede"))
        self.actionRechercheNonDecede.triggered.connect(lambda :self.openAfficher("Recherche des personnes non décédés","0Decede"))
         
        self.show()
    def openAfficher(self,msg,cr):
        self.Afficher = AfficherWindow(self.personnes,msg,cr)
        self.stack.addWidget(self.Afficher)
        self.openPage(self.Afficher)
    
    def openModifier(self,msg,cr):
        self.Modifier = ModifierPage(self.personnes,msg,cr)
        self.stack.addWidget(self.Modifier)
        self.openPage(self.Modifier)

    def openPage(self, page):
        self.stack.setCurrentWidget(page)
    
    def RPersonne(self):
        self.personnes.clear()
        with open(os.getcwd()+"/assets/data/personnes.csv") as file:
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
                        "Adresse": row[10]
                    })
        self.MiseAJour.setEnabled(True)
        msg = MessageBox("On a récupéré l'information situé dans le fichier personnes.csv")
    
    def EPersonne(self):
        with open(os.path.dirname(__file__)+"/assets/data/personnes.csv", mode="w") as file:
            headers = [k for k in self.personnes[0].keys()]
            writer = csv.DictWriter(csv,fieldnames=headers)
            writer.writeheader()
            writer.writerows(self.personnes)
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
