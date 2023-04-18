from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget
import os
class ModifierPage(QWidget):
    def __init__(self,personnes,msg,critere):
        super().__init__()
        path = os.path.dirname(__file__) + "/"
        ui_file = path+"modifier.ui"
        loadUi(ui_file, self)
        self.CIN.setFocus()
        self.afficheMode(critere=critere)
        self.lbl.setText(msg)
        self.returnBtn.clicked.connect(self.goHome)
        self.modifierBtn.clicked.connect(lambda: self.modifier(personnes,critere))
        self.show()
    
    def goHome(self):
        self.parent().setCurrentIndex(0)
    
    def modifier(self,personnes,critere):
        cin = self.CIN.text()
        val = self.cr.text()
        personnes[self.indicePers(personnes,cin)][critere] = val
        self.goHome()
    def indicePers(self,personnes,cin):
        cp=0
        for i in range(len(personnes)):
            if personnes[i]["CIN"]== cin:
                cp = i
                break
        return cp

    def afficheMode(self,critere):
        if(critere == "Tel"):
            self.cr.setInputMask("00 000 000")