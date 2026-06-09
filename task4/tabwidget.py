from PyQt5.QtWidgets import QTabWidget
import sys,os
from bookpage import bookPage
from authorpage import authorPage
from publpage import publPage

class tabWidget(QTabWidget):
    def __init__(self,library,parent=None):
        QTabWidget.__init__(self,parent)
        self.__bookPage=bookPage(library=library)
        self.addTab(self.__bookPage,u"книги")
        self.__authorPage=authorPage(library=library)
        self.addTab(self.__authorPage,u"авторы")
        self.__publPage=publPage(library=library)
        self.addTab(self.__publPage,u"издательства")
        self.currentChanged.connect(self.update)
    def update(self):
        self.__publPage.update()
        self.__authorPage.update()
        self.__bookPage.update()