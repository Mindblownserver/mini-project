from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget
from assets.widgets.messageBox import MessageBox
import os
class ModifierPage(QWidget):
    def __init__(self,personnes,cin,msg,critere):
        super().__init__()
        path = os.path.dirname(__file__) + "/"
        ui_file = path+"modifier.ui"
        loadUi(ui_file, self)
        self.tel=list()
        self.loadCle(personnes,cin)
        self.afficheMode(critere=critere)
        self.lbl.setText(msg)
        self.returnBtn.clicked.connect(self.goHome)
        self.modifierBtn.clicked.connect(lambda: self.modifier(personnes,cin,critere))
        self.show()
    
    def goHome(self):
        self.parent().setCurrentIndex(0)
    
    def loadCle(self,personnes,listeCIN):
        self.CIN.addItems(listeCIN)
        for personne in personnes:
            self.tel.append(personne["Tel"])

    def modifier(self,personnes,listeCIN,critere):
        cin = self.CIN.currentText()
        val = self.cr.text()
        if(critere=="Tel" and (val in self.tel or val =="")):
            msg =MessageBox("Error de modification","Le numéro du téléphone {} est déjà dans la base de données".format(val),"error")
            msg.exec_()
        else:
            personnes[self.indicePers(listeCIN,cin)][critere] = val
            msg =MessageBox("Opération a été un succès","Les données du patient {} a été modifiées".format(cin),"info")
            msg.exec_()
            self.goHome()
    def indicePers(self,listeCIN,cin):
        return listeCIN.index(cin)

    def afficheMode(self,critere):
        if(critere == "Tel"):
            self.cr.setInputMask("00 000 000")