from PyQt5.QtWidgets import QLabel,QHBoxLayout,QWidget
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore

class pixWidget(QWidget):
    def __init__(self,filename='',parent=None):
        QWidget.__init__(self,parent=parent)
        self.__hbox=QHBoxLayout()
        self.setLayout(self.__hbox)
        if filename:
            pixLabel=QLabel()
            pixLabel.setPixmap(QPixmap(filename).scaled(32, 32, QtCore.Qt.KeepAspectRatio))
            self.__hbox.addWidget(pixLabel)
            self.__hbox.addWidget(QLabel(filename))
            self.__hbox.addStretch()