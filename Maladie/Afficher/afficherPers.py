from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
import os

class AfficherMaladiesPersonnesPage(QWidget):
    def __init__(self,maladies):
        super().__init__()
        path = os.path.dirname(__file__) + "/"
        ui_file = path+"afficherPersonnes.ui"
        loadUi(ui_file, self)
        self.personnes = dict()
        self.loadData(maladies)
        self.listeOp.itemClicked.connect(lambda item: self.showData(item))
        self.returnBtn.clicked.connect(self.goHome)
        self.show()
    
    def goHome(self):
        self.parent().setCurrentIndex(0)
    
    def showData(self,item,personnesParCr):
        self.list.clear()
        for nom in personnesParCr[item.text()]:
            self.list.addItem(nom)
    def loadData(self,maladies):
        for maladie in maladies:
            if(maladie["CIN"] not in self.personnes.keys()):
                self.listeOp.addItem(maladie["CIN"])
                self.personnes[maladie["CIN"]] = [maladie["Maladie"]]
            else: self.personnes[maladie["CIN"]].append(maladie["Maladie"])
    
    def showData(self,item):
        self.list.clear()
        for nom in self.personnes[item.text()]:
            self.list.addItem(nom)