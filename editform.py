from PyQt5.QtWidgets import QWidget,QGridLayout,QVBoxLayout,QHBoxLayout,QPushButton,QLabel
from libwidget import libWidget

class editForm(QWidget,libWidget):
    def __init__(self,library=None,parent=None):
        QWidget.__init__(self,parent=parent)
        libWidget.__init__(self,library)
        self.__grid=QGridLayout()
        self.__vbox=QVBoxLayout()
        self.__hbox=QHBoxLayout()
        self.__vbox.addLayout(self.__grid)
        self.__vbox.addStretch(1)
        self.__hbox.addLayout(self.__vbox)
        self.setLayout(self.__hbox)
    def addLabel(self,text,x,y):self.__grid.addWidget(QLabel(text),x,y)
    def addNewWidget(self,widget,x,y):self.__grid.addWidget(widget,x,y)
    def addLeftLayout(self,layout):self.__hbox.insertLayout(0,layout)
    def setCurrentCode(self,value):
        self.__currentCode=value
        self.update()
    def getCurrentCode(self):return self.__currentCode
    def decode(self,qstring):return str(qstring.toUtf8()).decode('utf-8')
    def update(self):pass
