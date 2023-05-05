from PyQt5.QtWidgets import QWidget, QVBoxLayout
from assets.widgets.ThreeLineListItem import ListItem
from PyQt5.uic import loadUi
import os
class AffPersRisquePage(QWidget):
    def __init__(self,personnes,maladies):
        super().__init__()
        path = os.path.dirname(__file__) + "/"
        ui_file = path+"risque.ui"
        self.box = QVBoxLayout()
        loadUi(ui_file, self)
        for i in range(10):
            self.box.addWidget(ListItem("Yo","The name is unknown", f"{10+i}","11999019"))
        viewport = QWidget()
        viewport.setLayout(self.box)
        self.scroll.setWidget(viewport)
        self.returnBtn.clicked.connect(self.goHome)
        self.show()

    def goHome(self):
        self.parent().setCurrentIndex(0)