import csv
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
import os
# fetch data
personnes = [{}]
path = os.path.dirname(__file__) + "/"
with open(path+"personnes.csv") as file:
    reader = csv.reader(file, delimiter=",")
    lcount = 0
    for i, row in enumerate(reader):
        if i != 0:
            print(row[0])
# Affichage
table.setRowCount(len(personnes))
for row, personne in enumerate(personnes):
    table.setItem(row, 0, QTableWidgetItem(personne["CIN"]))
    table.setItem(row, 1, QTableWidgetItem(personne["NOM"]))
    table.setItem(row, 2, QTableWidgetItem(personne["PRENOM"]))
    table.setItem(row, 3, QTableWidgetItem(personne["TEL"]))
    table.setItem(row, 4, QTableWidgetItem(personne["NATIONALITE"]))
    table.setItem(row, 5, QTableWidgetItem(personne["AGE"]))
    table.setItem(row, 6, QTableWidgetItem(personne["JOUR"]))
app = QApplication([])
ui_file = path+"affichage.ui"
widget = loadUi(ui_file)
widget.show()
app.exec_()
