from PyQt5.QtWidgets import QMessageBox

class MessageBox(QMessageBox):
    def __init__(self,title,info,cr):
        super().__init__()
        self.setWindowTitle("Projet Corona")
        self.setText(title)
        self.setInformativeText(info)
        icon = self.Information
        if(cr!="info"):
            self.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
            self.setDefaultButton(QMessageBox.No)
            icon = self.Warning
        self.setIcon(icon)       
#  self.setDetailedText("details")