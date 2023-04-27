from PyQt5.QtWidgets import QWidget,QTableWidget,QTableWidgetItem
from PyQt5.uic import loadUi
import os

class MAfficherPage(QWidget):
    def __init__(self,maladies,nbrMaladies,listeMaladies,message,cr):
        super().__init__()
        path = os.path.dirname(__file__) + "/"
        ui_file = path+"afficher.ui" if cr.split()[-1] != "1" else path+"afficherPercent.ui"
        self.cr = cr.split()[0]
        self.maladies = maladies
        loadUi(ui_file, self)
        self.afficheMode(message,cr)
        self.showData(self.maladies) if cr.split()[-1] != "1" else self.showDataPerc(listeMaladies,nbrMaladies)
        self.rechercheBtn.clicked.connect(lambda: self.showData(self.rechercheClassic()))
        self.returnBtn.clicked.connect(self.goHome)
        self.show()
    
    def goHome(self):
        self.parent().setCurrentIndex(0)
    
    def afficheMode(self,msg,cr):
        if(self.cr=="Tout" or cr.split()[-1]=="1"):
            self.critere.hide()
        elif(self.cr=="nom"):
            self.msg.setInputMask("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            self.cr="Maladie"
        self.text.setText(msg)

    def rechercheClassic(self):
        text = self.msg.text()
        maladieCherche= list(dict())
        for maladie in self.maladies:
            if (text.lower() in maladie[self.cr].lower()):
                maladieCherche.append(maladie)          
        return maladieCherche
    
    def showData(self, maladies):
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setRowCount(len(maladies))
        for row, maladie in enumerate(maladies):
                self.table.setItem(row, 0, QTableWidgetItem(maladie["Code"]))
                self.table.setItem(row, 1, QTableWidgetItem(maladie["CIN"]))
                self.table.setItem(row, 2, QTableWidgetItem(maladie["Maladie"]))
                self.table.setItem(row, 3, QTableWidgetItem(maladie["nbrAn"])) 
    
    def showDataPerc(self,listeMaladies,taille):
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setRowCount(taille)
        for row, maladie in enumerate(listeMaladies):
                self.table.setItem(row, 0, QTableWidgetItem(maladie))
                self.table.setItem(row, 1, QTableWidgetItem(self.pourcentage(maladie)))
    
    def pourcentage(self,nom):
        cp=0
        for personne in self.maladies:
            if personne["Maladie"] == nom:
               cp+=1
        return str((cp/len(self.maladies))*100)
    
    
    """ self.parMaladie("8312655")
    def parMaladie(self, cin):
        print([i["Maladie"] for i in list(filter(lambda x: x["CIN"] == cin, self.maladies))]) """