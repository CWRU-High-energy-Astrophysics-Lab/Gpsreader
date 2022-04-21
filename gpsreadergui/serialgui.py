from serialinterface import portrw

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt, QSize, QThread, QObject, pyqtSignal
from PyQt5 import QtWidgets, uic
import sys
import serial.tools.list_ports



class GPS_Main(QMainWindow):
    def __init__(self):
        super(GPS_Main, self).__init__()
        loadUi("port_setting_gui_ui", self)
        self.applyButton.clicked.connect(self.applysettings)
        self.cancelButton.clicked.connect(self.cancelsettings)
        ports = serial.tools.list_ports.comports()
        for port, desc, hwid in sorted(ports):
            print("{}: {} [{}]".format(port, desc, hwid))

    def applysettings(self):
        pass
    def cancelsettings(self):
        pass