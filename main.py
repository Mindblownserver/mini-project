from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow,QStackedWidget,QWidget
import os
from Personne.Afficher.afficherTout import AfficherWindow
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
        self.stack.addWidget(self.Home)
        # Set the central widget to the stacked widget
        self.setCentralWidget(self.stack)
        
        self.actionAfficher.triggered.connect(lambda :self.openAfficher("Tout"))
        self.actionRechercheTel.triggered.connect(lambda :self.openAfficher("Recherche par numéro du Téléphone"))
        self.actionRechercheInd.triggered.connect(lambda :self.openAfficher("Recherche par indicatif"))
        self.actionRechercheNat.triggered.connect(lambda :self.openAfficher("Recherche par nationalité"))
        self.actionRechercheDecede.triggered.connect(lambda :self.openAfficher("Recherche des personnes décédés"))
        self.actionRechercheNonDecede.triggered.connect(lambda :self.openAfficher("Recherche des personnes non décédés"))
         
        self.show()
    def openAfficher(self,msg):
        self.Afficher = AfficherWindow(msg)
        self.stack.addWidget(self.Afficher)
        self.stack.setCurrentWidget(self.Afficher)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
