from PyQt5.QtWidgets import QMainWindow,QAction,QFileDialog
from PyQt5.QtGui import QIcon
import sys,os
from dataxml import dataxml
from accounting import accounting
from tabwidget import tabWidget

class mainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle(u'Учет внутриофисных расходов')
        self.setGeometry(100,100,800,600)
        self.__accounting=accounting()
        self.dataxml=dataxml(self.__accounting)
        self.tabWidget=tabWidget(self.__accounting,self)
        self.setCentralWidget(self.tabWidget)
        self.tabWidget.update()

        self.new=QAction(QIcon(),'New',self)
        self.new.setStatusTip('New database')
        self.new.triggered.connect(self.newAction)

        self.openxml=QAction(QIcon(),'Open XML',self)
        self.openxml.setStatusTip('Open data from XML')
        self.openxml.triggered.connect(self.openXMLAction)

        self.savexml=QAction(QIcon(),'Save XML',self)
        self.savexml.setStatusTip('Save data to XML')
        self.savexml.triggered.connect(self.saveXMLAction)

        self.menubar=self.menuBar()
        self.menufile=self.menubar.addMenu('&File')
        self.menufile.addAction(self.new)
        self.menufile.addSeparator()
        self.menufile.addAction(self.openxml)
        self.menufile.addSeparator()
        self.menufile.addAction(self.savexml)
        self.statusBar()
    def newAction(self):
        self.__accounting.clear()
        self.tabWidget.update()
    def openXMLAction(self):
        filename=QFileDialog.getOpenFileName(self,u'Открыть XML',os.getcwd(),u"*.xml")[0]
        if filename:
            self.__accounting.clear()
            self.dataxml.readFile(filename=filename)
            self.tabWidget.update()
    def saveXMLAction(self):
        filename=QFileDialog.getSaveFileName(self,u'Сохранить XML',os.getcwd(),u"*.xml")[0]
        if filename:self.dataxml.writeFile(filename=filename)
