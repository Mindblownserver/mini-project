from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
import os
class First(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        path = os.path.dirname(__file__) + "/"
        uic.loadUi(path+'first.ui', self)
