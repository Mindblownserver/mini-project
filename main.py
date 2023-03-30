from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow
import os

# Initialisation de l'application


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        path = os.path.dirname(__file__) + "/"
        ui_file = path+"GUI.ui"
        loadUi(ui_file, self)
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
