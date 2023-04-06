from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox,QApplication, QMainWindow,QStackedWidget,QWidget
import os
import csv
from Personne.Afficher.afficherTout import AfficherWindow
from Personne.Ajouter.ajouter import AjouterPage
# Initialisation de l'application

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        path = os.path.dirname(__file__) + "/"
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

        # Pages
        self.Home = HomePage()
        self.Ajouter = AjouterPage(self.personnes)
        self.stack.addWidget(self.Home)
        self.stack.addWidget(self.Ajouter)
        # Set the central widget to the stacked widget
        self.setCentralWidget(self.stack)
        
        # Mise à jour
        self.actionAjouter.triggered.connect(self.openAjouter)
        self.actionRPersonne.triggered.connect(self.RPersonne)
        # Recherche & afficher
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
        self.stack.setCurrentWidget(self.Afficher)
    def openAjouter(self):
        self.stack.setCurrentWidget(self.Ajouter)
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
                    })
        msg = QMessageBox()
        msg.setWindowTitle("Projet Corona")
        msg.setText("Opération a été un succès")
        msg.setIcon(QMessageBox.Information)
        msg.setDefaultButton(QMessageBox.Retry)
        msg.setInformativeText("On a récupéré l'information situé dans le fichier personnes.csv")
#        msg.setDetailedText("details")
        msg.exec_()

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
