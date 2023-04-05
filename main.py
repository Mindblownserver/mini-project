from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow,QStackedWidget,QWidget
import os
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
        self.stack = QStackedWidget(self)

        # Pages
        self.Home = HomePage()
        self.Ajouter = AjouterPage()
        self.stack.addWidget(self.Home)
        self.stack.addWidget(self.Ajouter)
        # Set the central widget to the stacked widget
        self.setCentralWidget(self.stack)
        
        # Mise à jour
        self.actionAjouter.triggered.connect(self.openAjouter)
        
        # Recherche & afficher
        self.actionAfficher.triggered.connect(lambda :self.openAfficher("Fiche des personnes malades","Tout"))
        self.actionRechercheTel.triggered.connect(lambda :self.openAfficher("Recherche par numéro du Téléphone","Tel"))
        self.actionRechercheInd.triggered.connect(lambda :self.openAfficher("Recherche par indicatif","indi"))
        self.actionRechercheNat.triggered.connect(lambda :self.openAfficher("Recherche par nationalité","Nationalite"))
        self.actionRechercheDecede.triggered.connect(lambda :self.openAfficher("Recherche des personnes décédés", "1Decede"))
        self.actionRechercheNonDecede.triggered.connect(lambda :self.openAfficher("Recherche des personnes non décédés","0Decede"))
         
        self.show()
    def openAfficher(self,msg,cr):
        self.Afficher = AfficherWindow(msg,cr)
        self.stack.addWidget(self.Afficher)
        self.stack.setCurrentWidget(self.Afficher)
    def openAjouter(self):
        self.stack.setCurrentWidget(self.Ajouter)
        
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
