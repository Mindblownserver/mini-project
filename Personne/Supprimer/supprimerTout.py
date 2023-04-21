from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from assets.widgets.messageBox import MessageBox
import os

class SupprimerToutPage(QWidget):
    def __init__(self,personnes,criteria):
        super().__init__()
        self.cr = self.afficheMode(criteria)
        self.lCr=dict()
        path = os.path.dirname(__file__) + "/"
        ui_file = path+"supprimerTout.ui"
        loadUi(ui_file, self)
        self.loadCr(personnes,self.cr)
        self.msg.setText(self.msg.text()+criteria+" donnée")
        self.listeOp.itemDoubleClicked.connect(lambda item: self.showData(item,self.lCr))
        self.returnBtn.clicked.connect(self.goHome)
        self.suppBtn.clicked.connect(lambda: self.deleteCr(personnes))
        self.show()
    
    def goHome(self):
        self.parent().setCurrentIndex(0)

    def afficheMode(self,criteria):
        if(criteria.split()[-1]=="Indicatif"):
            return "Tel"
        return "Nationalite"
    
    def loadCr(self,personnes,cr):
        for personne in personnes:
            if(personne[cr] not in self.lCr.keys()):
                self.listeOp.addItem(personne[cr])
                self.lCr[personne[cr]] = [f"{personne['Prenom']} {personne['Nom']}"]
            else:self.lCr[personne[cr]].append(f"{personne['Prenom']} {personne['Nom']}")

    def showData(self,item,personnesParCr):
        self.list.clear()
        for nom in personnesParCr[item.text()]:
            self.list.addItem(nom)
            # self.lCIN.append(personne["CIN"])

    def deleteCr(self,personnes):
        msg = MessageBox("Êtes vous sûre de l'opèration?","Tu vas perdre les données du patient {} {}".format(personnes[index]["Prenom"],personnes[index]["Nom"]),"critique")
        msg.buttonClicked.connect(lambda btn: self.popupBtn(btn,personnes))
        msg.exec_() 

    def popupBtn(self,btn,personnes):
        print(btn.text())
        if btn.text()[1:] == "Yes":
            pass
