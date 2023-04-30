from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget
from assets.widgets.messageBox import MessageBox
import os

class MModifierPage(QWidget):
    def __init__(self,msg,cr):
        super().__init__()
        path = os.path.dirname(__file__) + "/"
        ui_file = path+"modifier.ui"
        loadUi(ui_file, self)
        self.show()