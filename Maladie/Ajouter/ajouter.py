from PyQt5.QtWidgets import QWidget
from assets.widgets.messageBox import MessageBox
from PyQt5.uic import loadUi
import os
class MAjouterPage(QWidget):
    def __init__(self):
        super().__init__()
        path = os.path.dirname(__file__) + "/"
        ui_file = path+"ajouter.ui"
        loadUi(ui_file, self)
    