import os
import csv
from PyQt5.uic import loadUi 
from PyQt5.QtWidgets import QWidget,QApplication

class AjouterPage(QWidget):
    def __init__(self):
        super().__init__()
        path = os.path.dirname(__file__)+"/"
        ui_file = path+"ajouter.ui"
        loadUi(ui_file,self)
        self.returnBtn.clicked.connect(self.goHome)
        self.show()
    def goHome(self):
        self.parent().setCurrentIndex(0)
if __name__ == "__main__":
    app= QApplication([])
    widget = AjouterPage()
    app.exec_()