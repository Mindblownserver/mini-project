from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from assets.widgets.messageBox import MessageBox
import os

class SupprimerToutPage(QWidget):
    def __init__(self,personnes,maladies,criteria):
        super().__init__()
        self.lCr=dict()
        path = os.path.dirname(__file__) + "/"
        ui_file = path+"supprimerTout.ui"
        loadUi(ui_file, self)
        self.cr = self.afficheMode(personnes,criteria)
        self.msg.setText(self.msg.text()+criteria+" donnée")
        self.listeOp.itemClicked.connect(lambda item: self.showData(item,self.lCr))
        self.returnBtn.clicked.connect(self.goHome)
        self.suppBtn.clicked.connect(lambda: self.deleteCr(personnes,maladies))
        self.show()
    
    def goHome(self):
        self.parent().setCurrentIndex(0)

    def afficheMode(self,personnes,criteria):
        if(criteria.split()[-1]=="Indicatif"):
            self.loadInd(personnes,"Tel")
            return "Tel"
        self.loadNat(personnes,"Nationalite")
        return "Nationalite"
    
    def loadNat(self,personnes,cr):
        for personne in personnes:
            if(personne[cr] not in self.lCr.keys()):
                self.listeOp.addItem(personne[cr])
                self.lCr[personne[cr]] = [f"{personne['Prenom']} {personne['Nom']}"]
            else:self.lCr[personne[cr]].append(f"{personne['Prenom']} {personne['Nom']}")
    
    def loadInd(self,personnes,cr):
        for personne in personnes:
            if(personne[cr][:2] not in self.lCr.keys()):
                self.listeOp.addItem(personne[cr][:2])
                self.lCr[personne[cr][:2]] = [f"{personne['Prenom']} {personne['Nom']}"]
            else:self.lCr[personne[cr][:2]].append(f"{personne['Prenom']} {personne['Nom']}")

    def showData(self,item,personnesParCr):
        self.list.clear()
        for nom in personnesParCr[item.text()]:
            self.list.addItem(nom)
            # self.lCIN.append(personne["CIN"])

    def deleteCr(self,personnes,maladies):
        msg = MessageBox("Êtes vous sûre de l'opèration?","Tu vas perdre les données des personnes ayant cette critère pour toujours ","critique")
        msg.buttonClicked.connect(lambda btn: self.popupBtn(btn,personnes,maladies))
        msg.exec_() 

    def popupBtn(self,btn,personnes,maladies):
        item = self.listeOp.currentItem()
        if btn.text()[1:] == "Yes":
            cp=0
            self.listeOp.takeItem(self.listeOp.indexFromItem(item).row())
            self.list.clear()
            for i in range(len(personnes)):
                if(item.text() in personnes[i-cp][self.cr]): 
                    # Supprimer personne de la maladie
                    self.supprimerDeLaMaladie(personnes[i-cp]["CIN"],maladies)
                    del personnes[i-cp]
                    cp+=1
    
    def supprimerDeLaMaladie(self,CIN,maladies):
        cp=0
        for i in range(len(maladies)):
            if (maladies[i-cp]["CIN"]==CIN):
                t=maladies.pop(i-cp)
                print(t)
                cp+=1


""" if self.cr == "Nationalite":
                for i in range(len(personnes)):
                    if(personnes[i-cp][self.cr]== item.text()): 
                        del personnes[i-cp]
                        cp+=1
            else: """