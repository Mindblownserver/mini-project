from PyQt5.QtWidgets import QMessageBox

class MessageBox(QMessageBox):
    def __init__(self,title,info,cr):
        super().__init__()
        self.setWindowTitle("Projet Corona")
        self.setText(title)
        self.setIcon(QMessageBox.Information if cr == "info" else QMessageBox.warning)
        self.setDefaultButton(QMessageBox.Retry)
        self.setInformativeText(info)
#        self.setDetailedText("details")
        self.exec_() 