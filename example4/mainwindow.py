from PyQt5.QtWidgets import QMainWindow,QAction,QFileDialog
from PyQt5.QtGui import QIcon
import sys,os
sys.path.insert(0, "./library")
from datasql import datasql
from dataxml import dataxml
from datajson import datajson
from library import library
from tabwidget import tabWidget

class mainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle(u'Библиотека')
        self.__library=library()
        self.dataxml=dataxml(self.__library)
        self.datasql=datasql(self.__library)
        self.datajson=datajson(self.__library)
        self.tabWidget=tabWidget(self.__library,self)
        self.setCentralWidget(self.tabWidget)
        self.tabWidget.update()

        self.new=QAction(QIcon(),'New',self)
        self.new.setStatusTip('New database')
        self.new.triggered.connect(self.newAction)

        self.openxml=QAction(QIcon(),'Open XML',self)
        self.openxml.setStatusTip('Open data from XML')
        self.openxml.triggered.connect(self.openXMLAction)

        self.opensql=QAction(QIcon(),'Open SQL',self)
        self.opensql.setStatusTip('Open data from SQL')
        self.opensql.triggered.connect(self.openSQLAction)

        self.openjson=QAction(QIcon(),'Open JSON',self)
        self.openjson.setStatusTip('Open data from JSON')
        self.openjson.triggered.connect(self.openJSONAction)

        self.savexml=QAction(QIcon(),'Save XML',self)
        self.savexml.setStatusTip('Save data to XML')
        self.savexml.triggered.connect(self.saveXMLAction)

        self.savesql=QAction(QIcon(),'Save SQL',self)
        self.savesql.setStatusTip('Save data to SQL')
        self.savesql.triggered.connect(self.saveSQLAction)

        self.savejson=QAction(QIcon(),'Save JSON',self)
        self.savejson.setStatusTip('Save data to JSON')
        self.savejson.triggered.connect(self.saveJSONAction)

        self.menubar=self.menuBar()
        self.menufile=self.menubar.addMenu('&File')
        self.menufile.addAction(self.new)
        self.menufile.addSeparator()
        self.menufile.addAction(self.openxml)
        self.menufile.addAction(self.opensql)
        self.menufile.addAction(self.openjson)
        self.menufile.addSeparator()
        self.menufile.addAction(self.savexml)
        self.menufile.addAction(self.savesql)
        self.menufile.addAction(self.savejson)
        self.statusBar()
    def newAction(self):
        self.__library.clear()
        self.tabWidget.update()
    def openXMLAction(self):
        filename=QFileDialog.getOpenFileName(self,u'Открыть XML',os.getcwd(),u"*.xml")[0]
        if filename:
            self.__library.clear()
            self.dataxml.readFile(filename=filename)
            self.tabWidget.update()
    def openSQLAction(self):
        filename=QFileDialog.getOpenFileName(self,u'Открыть SQL',os.getcwd(),u"*.sqlite")[0]
        if filename:
            self.__library.clear()
            self.datasql.readFile(filename=filename)
            self.tabWidget.update()
    def openJSONAction(self):
        filename=QFileDialog.getOpenFileName(self,u'Открыть JSON',os.getcwd(),u"*.json")[0]
        if filename:
            self.__library.clear()
            self.datajson.readFile(filename=filename)
            self.tabWidget.update()
    def saveXMLAction(self):
        filename=QFileDialog.getSaveFileName(self,u'Сохранить XML',os.getcwd(),u"*.xml")[0]
        if filename:self.dataxml.writeFile(filename=filename)
    def saveSQLAction(self):
        filename=QFileDialog.getSaveFileName(self,u'Сохранить SQL',os.getcwd(),u"*.sqlite")[0]
        if filename:self.datasql.writeFile(filename=filename)
    def saveJSONAction(self):
        filename=QFileDialog.getSaveFileName(self,u'Сохранить JSON',os.getcwd(),u"*.json")[0]
        if filename:self.datajson.writeFile(filename=filename)