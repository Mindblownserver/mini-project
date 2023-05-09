from PyQt5.QtWidgets import QWidget, QVBoxLayout
from assets.widgets.ThreeLineListItem import ListItem
from PyQt5.uic import loadUi
import os
class AffPersRisquePage(QWidget):
    def __init__(self,personnes,maladies):
        super().__init__()
        path = os.path.dirname(__file__) + "/"
        ui_file = path+"risque.ui"
        loadUi(ui_file, self)
        # assigning layout to scroll area
        self.box = QVBoxLayout()
        # Loading list items
        self.loadListPersonnesARisques(personnes,maladies)
        viewport = QWidget()
        viewport.setLayout(self.box)
        self.scroll.setWidget(viewport)
        self.returnBtn.clicked.connect(self.goHome)
        self.show()

    def goHome(self):
        print(self.parent())
        self.parent().setCurrentIndex(0)
    
    def loadMaladies(self,maladies):
        res=dict()
        for maladie in maladies:
            if maladie["CIN"] not in res.keys():
                res[maladie["CIN"]] = [maladie["Maladie"]]
            else:res[maladie["CIN"]].append(maladie["Maladie"])
        return res
    def loadPersonnes(self,personnes):
        res=dict()
        for personne in personnes:
            if(personne["Decede"]=="0"):
                #{CIN:[NOM PRENOM, AGE]}
                res[personne["CIN"]] = [personne["Nom"],personne["Prenom"],int(personne["Age"])]
        return res
    
    def CalculRisqueDesPersonnes(self,dictPersonnes,dictMaladies):
        afficherDict=dict()
        for cinKey in dictPersonnes.keys():
            percentage=0
            if(cinKey in dictMaladies.keys()):
                percentage=percentage+20 if dictPersonnes[cinKey][-1] >70 else percentage+10 if 50<=dictPersonnes[cinKey][-1]<=70 else 0
                if "DIABETE" in dictMaladies[cinKey]:percentage=percentage+15
                if "HYPERTENSION" in dictMaladies[cinKey]: percentage=percentage+20
                if "ASTHME" in dictMaladies[cinKey]: percentage=percentage+20
            if percentage!=0:
                afficherDict[cinKey]=[dictPersonnes[cinKey][0],dictPersonnes[cinKey][1],dictPersonnes[cinKey][2],percentage]                
        print(afficherDict)
        return afficherDict
    def loadListPersonnesARisques(self,personnes,maladies):
        dictMaladies=self.loadMaladies(maladies)
        dictPersonnes = self.loadPersonnes(personnes)
        personnesARisques = self.CalculRisqueDesPersonnes(dictPersonnes,dictMaladies)
        for cinKey in personnesARisques.keys():
            self.box.addWidget(ListItem(personnesARisques[cinKey][0],personnesARisques[cinKey][1],personnesARisques[cinKey][2],cinKey,personnesARisques[cinKey][3],self.percentage))
""" 
        for i in range(10):
            self.box.addWidget(ListItem("Yo","The name is unknown", f"{10+i}","11999019",self.percentage)) """