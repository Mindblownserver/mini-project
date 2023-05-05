import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
import os
class ListItem(QWidget):
    def __init__(self,nom:str,prenom:str,age:str,cin:str):
        super().__init__()
        path = os.path.dirname(__file__) + "/"
        ui_file = path+"ThreeLineListItem.ui"
        loadUi(ui_file,self)
        # load Data
        self.nom.setText(f"{prenom} {nom}")
        self.cin.setText(cin)
        self.age.setText(f"{age} ans")
