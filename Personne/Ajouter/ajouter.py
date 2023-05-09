import os
from PyQt5.uic import loadUi 
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget
from assets.widgets.messageBox import *
class AjouterPage(QWidget):
    def __init__(self,personnes):
        super().__init__()
        path = os.path.dirname(__file__)+"/"
        ui_file = path+"ajouter.ui"
        loadUi(ui_file,self)
        self.LDate.setMaximumDate(QDate.currentDate())
        self.show()
        self.cin=list()
        self.tel=list()
        self.loadCle(personnes)
        self.ajouterBtn.clicked.connect(lambda : self.ajouter(personnes=personnes))
        self.returnBtn.clicked.connect(self.goHome)
        
    def goHome(self):
        self.parent().setCurrentIndex(0)
    def loadCle(self,personnes):
        nat=set()
        for personne in personnes:
            self.cin.append(personne["CIN"])
            nat.add(personne["Nationalite"])
            self.tel.append(personne["Tel"])
        # Load nationalités
        self.nat.addItems(list(nat))
    def ajouter(self,personnes):
        #Enregistrer le dictionnaire
        nom = self.Lnom.text()
        prenom = self.Lprenom.text()
        nat = self.nat.currentText().upper()
        age = str(self.LAge.value())
        tel = str(self.LTel.value())
        cin = self.LCIN.text()
        adr = self.LAdr.text()
        date = self.LDate.text().split("/")
        day,month,year = date[0],date[1],date[2]
        decede = "1" if self.dead.isChecked() else "0"
        if(nom=="" or prenom=="" or age=="" or tel=="" or cin=="" or adr=="" or len(date)==0):
            msg =MessageBox("Prière de remplir tous les champs","","error")
            msg.exec_() 
        elif((nat =="-Nationalité-".upper()) or (not (cin.isdigit() and nom.isalpha() and prenom.isalpha()))):
            msg =MessageBox("Veuillez vérifier les données mis","","error")
            msg.exec_()
        elif(cin in self.cin or tel in self.tel):
            msg =MessageBox("Numéro CIN ou téléphone éxiste déjà","","error")
            msg.exec_()
        else:
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
            
            msg = MessageBox("Opération éxecuté avec succès","Le patient {} {} a été ajouté!".format(nom,prenom),"info")
            msg.exec_() 
            self.goHome()
    
    """ 
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
    """