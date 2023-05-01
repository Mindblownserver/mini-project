from PyQt5.QtWidgets import QWidget,QApplication, QMainWindow,QStackedWidget
from Personne.modifer.modifier import ModifierPage
from Personne.Afficher.afficherTout import AfficherWindow
from Personne.Ajouter.ajouter import AjouterPage
from Personne.Supprimer.supprimer import SupprimerPage  
from Personne.Supprimer.supprimerTout import SupprimerToutPage
from Maladie.Afficher.afficher import MAfficherPage
from Maladie.Afficher.afficherPers import AfficherMaladiesPersonnesPage
from Maladie.Ajouter.ajouter import MAjouterPage
from Maladie.Supprimer.supprimer import MSupprimerPage
from Maladie.Modifier.modifier import MModifierPage
from assets.widgets.messageBox import MessageBox
from PyQt5.uic import loadUi
import os
import csv

# Initialisation de l'application

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        path = os.path.dirname(__file__) + "/Home/"
        ui_file = path+"home.ui"
        loadUi(ui_file, self)
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        path = os.path.dirname(__file__) + "/"
        ui_file = path+"GUI.ui"
        loadUi(ui_file, self)
        self.cmp = 0
        self.personnes = list(dict())
        self.maladies=list(dict())
        self.nomMaladies = set()
        self.stack = QStackedWidget(self)
        self.MiseAJour.setEnabled(False)
        self.Gestion.setEnabled(False)
        self.Calcul.setEnabled(False)
        self.actionEnre.setEnabled(False)
        # Pages
        self.Home = HomePage()

        self.stack.addWidget(self.Home)
        self.stack.setContentsMargins(0,0,0,0)
        #fdsfsdfdsfsdf
    # Set the central widget to the stacked widget
        self.setCentralWidget(self.stack)
        # Mise à jour menu  
        ## Ajouter
        self.actionAjouter.triggered.connect(self.openAjouter)
        self.actionAjMal.triggered.connect(lambda: self.openMaladie("ajouter"))
        ## Modifier
        self.actionTel.triggered.connect(lambda: self.openModifier("Téléphone","Tel"))
        self.actionAdresse.triggered.connect(lambda: self.openModifier("Adresse","Adresse"))
        self.actionModAnnMal.triggered.connect(lambda: self.openModifierMal("Nombre d'année","nbrAn"))
        self.actionModDecMal.triggered.connect(lambda: self.openModifierMal("Décès (0: vivant, 1:mort)","Decede"))
        ## Supprimer
        self.actionSuppPers.triggered.connect(lambda: self.openSupprimer())
        self.actionSuppNat.triggered.connect(lambda: self.openSupprimer("une Nationalité"))
        self.actionSuppInd.triggered.connect(lambda: self.openSupprimer("un Indicatif"))
        self.actionSuppMal.triggered.connect(lambda: self.openMaladie("supprimer"))
        ## Récuperer & Enregistrer
        self.actionRecu.triggered.connect(self.recuperation)
        self.actionEnre.triggered.connect(self.enregistrement)
        # Recherche & afficher menu
        self.actionAfficher.triggered.connect(lambda :self.openAfficher("Fiche des personnes malades","Tout"))
        self.actionAffMaladie.triggered.connect(lambda: self.openAfficherMaladie("Fiche des maladies","Tout"))
        self.actionRechercheTel.triggered.connect(lambda :self.openAfficher("Recherche par numéro du Téléphone","Tel"))
        self.actionRechercheInd.triggered.connect(lambda :self.openAfficher("Recherche par indicatif","indi"))
        self.actionRechercheNat.triggered.connect(lambda :self.openAfficher("Recherche par nationalité","Nationalite"))
        self.actionRechercheDecede.triggered.connect(lambda :self.openAfficher("Recherche des personnes décédés par leurs numéro du téléphone", "Tel","1"))
        self.actionRechercheNonDecede.triggered.connect(lambda :self.openAfficher("Recherche des personnes non décédés par leurs numéro du téléphone","Tel","0"))
        self.actionRechercheMal.triggered.connect(lambda: self.openAfficherMaladie("Recherche par une maladie","nom 0")) 
        self.actionRechercheMalPerc.triggered.connect(lambda: self.openAfficherMaladie("Recherche par une maladie","nom 1"))
        self.actionRecherchePers.triggered.connect(lambda: self.openAfficherMaladie("Recherche les maladies d'une personne par CIN","CIN"))
        self.actionRechercheMalPers.triggered.connect(self.openAfficherMaladiePersonne)

        self.show()
    
    def openModifierMal(self,msg,cr):
        persMal = self.maladies if cr=="nbrAn" else self.personnes
        self.Modifier=MModifierPage(persMal,msg,cr)
        self.openPage(self.Modifier)
    
    def openAjouter(self):
        self.Ajouter = AjouterPage(self.personnes,self.cmp)
        self.cmp+=1
        print(self.cmp)
        self.openPage(self.Ajouter)

    def openMaladie(self,msg):
        if(msg =="ajouter"):
            cin=[personne["CIN"] for personne in self.personnes]
            print(cin)
            self.page= MAjouterPage(self.maladies,self.nomMaladies,cin)
        elif(msg=="supprimer"):
            self.page= MSupprimerPage(self.maladies,self.nomMaladies)
        self.openPage(self.page)


    def openAfficher(self,msg,cr,st=""):
        self.Afficher = AfficherWindow(self.personnes,msg,cr,st)
        self.openPage(self.Afficher)

    def openAfficherMaladiePersonne(self):
        self.Afficher = AfficherMaladiesPersonnesPage(self.maladies)
        self.openPage(self.Afficher)

    def openAfficherMaladie(self,msg,cr):
        taille = len(self.maladies) if cr.split()[-1] != "1" else len(self.nomMaladies)
        self.MAfficher = MAfficherPage(self.maladies,taille,list(self.nomMaladies),msg,cr)
        self.openPage(self.MAfficher)
    
    def openSupprimer(self,cr=""):
        if(cr==""):
            self.Supprimer = SupprimerPage(self.personnes)
        else:
            self.Supprimer = SupprimerToutPage(self.personnes, cr)
        self.openPage(self.Supprimer)
    
    def openModifier(self,msg,cr):
        cin=[personne["CIN"] for personne in self.personnes]
        self.Modifier = ModifierPage(self.personnes,cin,msg,cr)
        self.openPage(self.Modifier)

    def openPage(self, page):
        self.stack.addWidget(page)
        self.stack.setCurrentWidget(page)
    
    def recuperation(self):
        self.RMaladies()
        self.RPersonne()
        self.Gestion.setEnabled(True)
        self.MiseAJour.setEnabled(True)
        self.actionEnre.setEnabled(True)
        self.actionRecu.setEnabled(False)
        self.Calcul.setEnabled(True)
        msg = MessageBox("Opération a été un succès","On a récupéré des informations","info")
        msg.exec_() 

    def enregistrement(self):
        self.EPersonne()
        self.EMaladies()
        msg = MessageBox("Opération a été un succès","On a enregistré des informations!","info")
        msg.exec_() 
    
    def RPersonne(self):
        with open(os.getcwd()+"/assets/data/personnes.csv") as file:
            reader = csv.reader(file, delimiter=",")
            for i, row in enumerate(reader):
                if i != 0:
                    self.personnes.append({
                        "CIN": row[0],
                        "Nom": row[1],
                        "Prenom": row[2],
                        "Tel": row[3],
                        "Nationalite": row[4],
                        "Age": row[5],
                        "Jour": row[6],
                        "Mois": row[7],
                        "Annee": row[8],
                        "Decede": row[9],
                        "Adresse": row[10],
                    })
    def EPersonne(self):
        with open(os.path.dirname(__file__)+"/assets/data/personnes.csv", mode="w") as file:
            headers = ["CIN","Nom","Prenom","Tel","Nationalite","Age","Jour","Mois","Annee","Decede","Adresse"]
            writer = csv.DictWriter(file,fieldnames=headers)
            writer.writeheader()
            writer.writerows(self.personnes)
          
    def RMaladies(self):
        with open(os.getcwd()+"/assets/data/maladies.csv") as file:
            reader = csv.reader(file, delimiter=",")
            for i, row in enumerate(reader):
                if i != 0:
                    self.maladies.append({
                        "Code": str(i),
                        "CIN": row[1],
                        "Maladie": row[2],
                        "nbrAn": row[3],
                    })
                    self.nomMaladies.add(row[2])
        
                
    def EMaladies(self):
        with open(os.path.dirname(__file__)+"/assets/data/maladies.csv", mode="w") as file:
            headers = ["Code","CIN","Maladie","nbrAn"]
            writer = csv.DictWriter(file,fieldnames=headers)
            writer.writeheader()
            writer.writerows(self.maladies)
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()