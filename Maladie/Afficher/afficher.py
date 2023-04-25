from PyQt5.QtWidgets import QWidget,QTableWidget,QTableWidgetItem
from PyQt5.uic import loadUi
import os

class MAfficherPage(QWidget):
    def __init__(self,maladies,nbrMaladies,listeMaladies,message,cr):
        super().__init__()
        path = os.path.dirname(__file__) + "/"
        ui_file = path+"afficher.ui" if cr.split()[-1] != "1" else path+"afficherPercent.ui"
        self.cr = cr.split()[0]
        loadUi(ui_file, self)
        self.afficheMode(message)
        self.showData(maladies,nbrMaladies,listeMaladies)
        self.rechercheBtn.clicked.connect(lambda: self.showData(self.rechercheClassic(maladies),nbrMaladies,listeMaladies))
        self.returnBtn.clicked.connect(self.goHome)
        self.show()
    
    def goHome(self):
        self.parent().setCurrentIndex(0)
    
    def afficheMode(self,msg):
        if(self.cr=="Tout"):
            self.critere.hide()
        elif(self.cr=="nom"):
            self.msg.setInputMask("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            self.cr="Maladie"
        self.text.setText(msg)
    
    def rechercheClassic(self,maladies):
        text = self.msg.text()
        maladieCherche= list(dict())
        for maladie in maladies:
            if (text.lower() in maladie[self.cr].lower()):
                maladieCherche.append(maladie)          
        return maladieCherche
    
    def showData(self, maladies,taille,listeMaladies):
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setRowCount(taille)
        if(taille!=len(maladies)):
            for row, maladie in enumerate(listeMaladies):
                    self.table.setItem(row, 0, QTableWidgetItem(maladie))
                    self.table.setItem(row, 1, QTableWidgetItem(self.pourcentage(maladies,maladie)))
                    
        else:
            for row, maladie in enumerate(maladies):
                    self.table.setItem(row, 0, QTableWidgetItem(maladie["Code"]))
                    self.table.setItem(row, 1, QTableWidgetItem(maladie["CIN"]))
                    self.table.setItem(row, 2, QTableWidgetItem(maladie["Maladie"]))
                    self.table.setItem(row, 3, QTableWidgetItem(maladie["nbrAn"])) 
    def pourcentage(self,maladies,nom):
        cp=0
        for personne in maladies:
            if personne["Maladie"] == nom:
               cp+=1
        return str((cp/len(maladies))*100)
    
    
    """ self.parMaladie("8312655")
    def parMaladie(self, cin):
        print([i["Maladie"] for i in list(filter(lambda x: x["CIN"] == cin, self.maladies))]) """