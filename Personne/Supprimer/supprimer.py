from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget
import os

class SupprimerPage(QWidget):
    def __init__(self,personnes):
        super().__init__()
        path = os.path.dirname(__file__) + "/"
        ui_file = path+"supprimer.ui"
        loadUi(ui_file, self)
        self.returnBtn.clicked.connect(self.goHome)
        self.show()
    
    def goHome(self):
        self.parent().setCurrentIndex(0)