from PyQt5.QtWidgets import QMessageBox

class MessageBox(QMessageBox):
    def __init__(self,info):
        super().__init__()
        self.setWindowTitle("Projet Corona")
        self.setText("Opération a été un succès")
        self.setIcon(QMessageBox.Information)
        self.setDefaultButton(QMessageBox.Retry)
        self.setInformativeText(info)
#        self.setDetailedText("details")
        self.exec_() 