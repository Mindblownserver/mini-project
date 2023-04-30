from PyQt5.QtWidgets import QWidget
from assets.widgets.messageBox import MessageBox
from PyQt5.uic import loadUi
import os
class MSupprimerPage(QWidget):
    def __init__(self,maladies,nMaladies):
        super().__init__()
        self.cinM = dict()
        path = os.path.dirname(__file__) + "/"
        ui_file = path+"supprimer.ui"
        loadUi(ui_file, self)
        self.loadData(maladies,nMaladies)
        self.listeOp.itemClicked.connect(lambda item: self.showData(item,self.cinM))
        self.suppBtn.clicked.connect(lambda: self.delete(maladies))
        self.returnBtn.clicked.connect(self.goHome)
        self.show()
    
    def goHome(self):
        self.parent().setCurrentIndex(0)

    def loadData(self,maladies,nomMaladies):
        self.listeOp.clear()
        self.listeOp.addItems(list(nomMaladies))
        for maladie in maladies:
            if maladie["Maladie"] not in self.cinM.keys():
                self.cinM[maladie["Maladie"]] = [maladie["CIN"]]
            else:self.cinM[maladie["Maladie"]].append(maladie["CIN"])
    
    def showData(self,item,cinM):
        self.list.clear()
        self.list.addItems(cinM[item.text()])
    def delete(self,maladies):
        msg = MessageBox("Êtes vous sûre de l'opèration?"," ","critique")
        msg.buttonClicked.connect(lambda btn: self.popupBtn(btn,maladies))
        msg.exec_() 
    def popupBtn(self,btn,maladies):
        item = self.listeOp.currentItem()
        if btn.text()[1:] == "Yes":
            self.listeOp.takeItem(self.listeOp.indexFromItem(item).row())
            self.list.clear()
            #print(item.text()) => nom de la maladie
            #delete from Maladies
            for i in range(len(maladies)):
                if maladies[i]["Maladie"] == item.text():
                    del maladies[i]