from PyQt5 import QtWidgets, uic
import os
class Page1(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self)
        path = os.path.dirname(__file__) + "/"
        uic.loadUi(path+'first.ui', self)

class Page2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self)
        path = os.path.dirname(__file__) + "/"
        uic.loadUi(path+'second.ui', self)

class App(QtWidgets.QMainWindow):
        def __init__(self):
            QtWidgets.QMainWindow.__init__(self)

            wid = Page1()

            self.grid = QtWidgets.QGridLayout()
            self.grid.addWidget(wid,0,0)
            self.frame.setLayout(self.grid)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = App()
    window.show()
    app.exec_()
