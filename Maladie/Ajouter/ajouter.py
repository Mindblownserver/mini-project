from PyQt5.QtWidgets import QWidget
from assets.widgets.messageBox import MessageBox
from PyQt5.uic import loadUi
import os
class MAjouterPage(QWidget):
    def __init__(self,maladies,nomMaladies,listeCin):
        super().__init__()
        self.cinM = dict()
        path = os.path.dirname(__file__) + "/"
        ui_file = path+"ajouter.ui"
        loadUi(ui_file, self)
        self.loadData(maladies,nomMaladies,listeCin)
        self.ajouterBtn.clicked.connect(lambda: self.ajouter(maladies,nomMaladies))
        self.returnBtn.clicked.connect(self.goHome)
        self.show()
    def goHome(self):
        self.parent().setCurrentIndex(0)

    def loadData(self,maladies,nom,cin):
        self.nMaladie.addItems(list(nom))
        self.CIN.addItems(cin)
        for maladie in maladies:
            if maladie["Maladie"] not in self.cinM.keys():
                self.cinM[maladie["Maladie"]] = [maladie["CIN"]]
            else:self.cinM[maladie["Maladie"]].append(maladie["CIN"])

    def ajouter(self,maladies,nomMaladies):
        nomMaladie = self.nMaladie.currentText()
        cin = self.CIN.currentText()
        an = str(self.nbrAn.value())
        index = str(int(maladies[-1]["Code"])+1)
        nomMaladies.add(nomMaladie)
        if(nomMaladie=="-Choisir une maladie-"):
            msg = MessageBox("Choisissez une maladie pour le patient","","error")
            msg.exec_()
        elif(cin == "-Choisir une CIN-" or cin == ""):
            msg = MessageBox("Erreur 404: utilisateur introvable","Veuillez verifier la CIN","error")
            msg.exec_()
        elif(cin == self.cinM[nomMaladie]):
            msg = MessageBox(f"Erreur de redondance","Le patient ayant {cin} souffre déjà de la maladie {nomMaladie}","error")
            msg.exec_()
        else:
            maladies.append({
                "Code": index,
                "CIN": cin,
                "Maladie": nomMaladie,
                "nbrAn":an
            })
            msg = MessageBox("La maladie {} du patient {} a été ajouté!".format(nomMaladie,cin),"","info")
            msg.exec_()
            self.goHome()
            
    