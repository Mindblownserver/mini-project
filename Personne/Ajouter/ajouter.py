import os
from PyQt5.uic import loadUi 
from PyQt5.QtWidgets import QWidget,QApplication
from assets.widgets.messageBox import *
class AjouterPage(QWidget):
    def __init__(self,personnes,cmp):
        super().__init__()
        path = os.path.dirname(__file__)+"/"
        ui_file = path+"ajouter.ui"
        loadUi(ui_file,self)
        self.show()
        self.cin=list()
        self.tel=list()
        self.loadCle(personnes,cmp)
        self.returnBtn.clicked.connect(self.goHome)
        self.ajouterBtn.clicked.connect(lambda : self.ajouter(personnes=personnes))
        self.generate.clicked.connect(lambda: self.generer(personnes))

        
    def goHome(self):
        self.parent().setCurrentIndex(0)
    def loadCle(self,personnes,cmp):
        for personne in personnes:
            self.cin.append(personne["CIN"])
            self.tel.append(personne["Tel"])
        # Information
        if cmp == 0:
            msg =MessageBox("Le caractére espace belle et bien existe!","Dans les champs 'Nom' et 'Prenom', Il suffit de mettre une lettre en majuscule pour insèrer l'espace entre ce dernier et le lettre en arrière ","info")
            msg.exec_() 
    def ajouter(self,personnes):
        #Enregistrer le dictionnaire
        nom = self.seperateWords(self.Lnom.text())
        prenom = self.seperateWords(self.Lprenom.text())
        nat = self.LNat.text()
        age = self.LAge.text()
        tel = self.LTel.text()
        cin = self.LCIN.text()
        adr = self.LAdr.text()
        date = self.LDate.text().split("/")
        day,month,year = date[0],date[1],date[2]
        decede = "1" if self.dead.isChecked() else "0"
        if(nat ==""or nom=="" or prenom=="" or age=="" or tel=="" or cin=="" or adr=="" or len(date)==0):
            msg =MessageBox("Il ya une insuffisance des données","Veuillez vérifier les données que vous avez mis","error")
            msg.exec_() 
        elif(cin in self.cin or tel in self.tel):
            msg =MessageBox("Il ya une ambiguité des données","Votre CIN ou numéro du téléphone est déjà enrgegistré dans la base de données","error")
            msg.exec_()
        else:
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
                msg = MessageBox("Le patient {} {} a été ajouté!".format(nom,prenom),"","info")
                msg.exec_() 
            except:
                msg = MessageBox("Le patient {} {} n'a pas été ajouté!".format(nom,prenom),"","info")
                msg.setIcon(QMessageBox.critical)
                msg.exec_() 
            finally:
                self.goHome()
    def generer(self,personnes):
        personnes.append({
                "CIN": "13213423",
                "Nom": "Kharrat",
                "Prenom": "Mohamed Yassine",
                "Tel": "87 654 345",
                "Nationalite": "Tun",
                "Age": "42",
                "Jour": "12",
                "Mois": "12",
                "Annee":"2341",
                "Decede": "0",
                "Adresse": "DSQDSQD"
            })
        self.goHome()

    def seperateWords(self,text):
        res=""
        for char in text:
            if(char.isupper()):
                res+= " "+char
            else:
                res+=char
        return res.lstrip() 