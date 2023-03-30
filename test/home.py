from PyQt5 import QtWidgets, uic
import os
class Page1(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        path = os.path.dirname(__file__) + "/"
        uic.loadUi(path+'first.ui', self)

class Page2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        path = os.path.dirname(__file__) + "/"
        uic.loadUi(path+'second.ui', self)

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Multi-Page App')

        # Create a stacked widget to manage pages
        self.stacked_widget = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # Add pages to the stacked widget
        self.page1 = Page1()
        self.stacked_widget.addWidget(self.page1)

        self.page2 = Page2()
        self.stacked_widget.addWidget(self.page2)

        # Connect signals and slots to switch between pages
        self.page1.pushButton.clicked.connect(self.switch_to_page2)
        self.page2.pushButton.clicked.connect(self.switch_to_page1)

    def switch_to_page1(self):
        self.stacked_widget.setCurrentWidget(self.page1)

    def switch_to_page2(self):
        self.stacked_widget.setCurrentWidget(self.page2)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = App()
    window.show()
    app.exec_()
