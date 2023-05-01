from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget
from assets.widgets.messageBox import MessageBox
import os

class MModifierPage(QWidget):
    def __init__(self,persMal,msg,cr):
        super().__init__()
        path = os.path.dirname(__file__) + "/"
        ui_file = path+"modifier.ui"
        self.cinM=dict()
        loadUi(ui_file, self)
        self.afficheMod(msg,cr)
        self.loadCle(persMal,cr)
        self.loadData()
        self.returnBtn.clicked.connect(self.goHome)
        self.CIN.currentTextChanged.connect(lambda item: self.loadMaladie(item))
        self.modifierBtn.clicked.connect(lambda: self.modifier(persMal,cr))
        self.show()

    def loadCle(self,persMals,cr):
        for persMal in persMals:
            if(cr=="nbrAn"):
                if persMal["CIN"] not in self.cinM.keys():
                    self.cinM[persMal["CIN"]] = [persMal["Maladie"]]
                else:self.cinM[persMal["CIN"]].append(persMal["Maladie"])   
            else:
                self.cinM[persMal["CIN"]] =[]
    def loadData(self):
        self.CIN.addItems(list(self.cinM.keys()))

    def loadMaladie(self,item):
        print(item)
        self.maladie.clear()
        self.maladie.addItems(self.cinM[item])

    def modifier(self,persMal,cr):
        cp=0
        cin = self.CIN.currentText()
        mal = self.maladie.currentText()
        val = str(self.cr.value())
        if(cr=="nbrAn"):
            index =self.indexOfDictNbrAnn(cin,maladie=mal)
            for maladie in persMal:
                if(maladie["CIN"]==cin):
                    if(cp==index):
                        maladie["nbrAn"]= val
                    cp+=1
                
        else:
            index = self.indexOfDictDecede(cin)
            persMal[index][cr]=val
        msg =MessageBox("Opération a été un succès","Les données du patient {} ont été modifiées".format(cin),"info")
        msg.exec_()
        self.goHome()
    def afficheMod(self,msg,cr):
        if (cr=="Decede"):
            self.maladieFrame.hide()
            self.cr.setMinimum(0)
            self.cr.setMaximum(1)
        self.crLbl.setText(msg)

    def goHome(self):
        self.parent().setCurrentIndex(0)

    def indexOfDictDecede(self,key):
        for i,element in enumerate(self.cinM):
            if(element == key):
                return i

    def indexOfDictNbrAnn(self,cin,maladie):
        return self.cinM[cin].index(maladie)