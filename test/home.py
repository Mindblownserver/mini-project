from PyQt5.QtWidgets import QMainWindow,QWidget,QApplication,QStackedWidget
from PyQt5.uic import loadUi
import os
class Page1(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('/home/yassine/project/2023/mini-project/Personne/Afficher/affichageUi.ui',self)
class App(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a stacked widget to hold the pages
        self.stack = QStackedWidget(self)

        # Create the pages and add them to the stack
        self.page1 = Page1()
        self.stack.addWidget(self.page1)
        # Set the stacked widget as the central widget
        self.setCentralWidget(self.stack)
if __name__ == '__main__':
    app = QApplication([])
    window = App()
    window.show()
    app.exec_()
