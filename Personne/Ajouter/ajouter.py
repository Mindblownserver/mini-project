import os
from PyQt5.uic import loadUi 
from PyQt5.QtWidgets import QWidget,QApplication
from assets.widgets.messageBox import *
class AjouterPage(QWidget):
    def __init__(self,personnes):
        super().__init__()
        path = os.path.dirname(__file__)+"/"
        ui_file = path+"ajouter.ui"
        loadUi(ui_file,self)
        self.returnBtn.clicked.connect(self.goHome)
        self.ajouterBtn.clicked.connect(lambda : self.ajouter(personnes=personnes))

        self.show()
    def goHome(self):
        self.parent().setCurrentIndex(0)
    def ajouter(self,personnes):
        # Controle de saisie

        #Enregistrer le dictionnaire
        nom = self.Lnom.text()
        prenom = self.Lprenom.text()
        nat = self.LNat.text()
        age = self.LAge.text()
        tel = self.LTel.text()
        cin = self.LCIN.text()
        adr = self.LAdr.text()
        date = self.LDate.text().split("/")
        day,month,year = date[0],date[1],date[2]
        decede = 1 if self.dead.isChecked() else 0
        try:
            personnes.append({
                "CIN": cin,
                "Nom": nom,
                "Prenom": prenom,
                "Tel": tel,
                "Nationalite": nat,
                "Age": age,
                "Jour": day,
                "Mois": month,
                "Annee":year,
                "Decede": decede,
                "Adresse": adr
            })
            msg = MessageBox("Le patient {} {} a été ajouté!".format(nom,prenom))
        except:
            msg = MessageBox("Le patient {} {} n'a pas été ajouté!".format(nom,prenom))
            msg.setIcon(QMessageBox.critical)
        finally:
            self.parent().setCurrentIndex(0)
if __name__ == "__main__":
    app= QApplication([])
    widget = AjouterPage()
    app.exec_()