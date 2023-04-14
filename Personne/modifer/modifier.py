from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget
import os
class ModifierPage(QWidget):
    def __init__(self,personnes,msg,critere):
        super().__init__()
        path = os.path.dirname(__file__) + "/"
        ui_file = path+"modifier.ui"
        loadUi(ui_file, self)
        self.lbl.setText(msg)
        self.returnBtn.clicked.connect(self.goHome)
        self.show()
    def goHome(self):
        self.parent().setCurrentIndex(0)
