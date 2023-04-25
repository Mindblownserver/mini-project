from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget
from assets.widgets.messageBox import MessageBox
import os
class ModifierPage(QWidget):
    def __init__(self,personnes,msg,critere):
        super().__init__()
        path = os.path.dirname(__file__) + "/"
        ui_file = path+"modifier.ui"
        loadUi(ui_file, self)
        self.cin=list()
        self.tel=list()
        self.loadCle(personnes)
        self.afficheMode(critere=critere)
        self.lbl.setText(msg)
        self.returnBtn.clicked.connect(self.goHome)
        self.modifierBtn.clicked.connect(lambda: self.modifier(personnes,critere))
        self.show()
    
    def goHome(self):
        self.parent().setCurrentIndex(0)
    
    def loadCle(self,personnes):
        for personne in personnes:
            self.cin.append(personne["CIN"])
            self.tel.append(personne["Tel"])

    def modifier(self,personnes,critere):
        cin = self.CIN.text()
        val = self.cr.text()
        if(cin not in self.cin):
            msg =MessageBox("Erreur 404","La personne ayant la CIN {} est introuvable dans la base de données".format(cin),"error")
            msg.exec_() 
        else:
            if(critere=="Tel" and val in self.tel):
                msg =MessageBox("Error de modification","Le numéro du téléphone {} est déjà dans la base de données".format(val),"error")
                msg.exec_()
            else:
                personnes[self.indicePers(personnes,cin)][critere] = val
                msg =MessageBox("Opération a été un succès","Les données du patient {} a été modifiées".format(cin),"info")
                msg.exec_()
                self.goHome()
    def indicePers(self,personnes,cin):
        cp=0
        for i in range(len(personnes)):
            if personnes[i]["CIN"]== cin:
                cp = i
                break
        return cp

    def afficheMode(self,critere):
        if(critere == "Tel"):
            self.cr.setInputMask("00 000 000")