from time import sleep
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt, QSize, QThread, QObject, pyqtSignal
from PyQt5 import QtWidgets, uic
import sys



class GPS_Main(QMainWindow):
    def __init__(self):
        super(GPS_Main, self).__init__()
        loadUi("welcomescreen.ui", self)
        self.login.clicked.connect(self.gotologin)
        self.create.clicked.connect(self.gotocreate)

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = GPS_Main()
    main.updatetest(100)


    sys.exit(app.exec_())

