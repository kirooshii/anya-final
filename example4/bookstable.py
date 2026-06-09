from PyQt5.QtWidgets import QTableWidgetItem,QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from dbtablewidget import dbTableWidget
from pixwidget import pixWidget

class booksTable(dbTableWidget):
    def __init__(self,library,parent=None):
        dbTableWidget.__init__(self,library=library,parent=parent,header=[u'название',u'обложка',u'авторы',u'издательство',u'год',u'страницы'])
    def setData(self):
        self.setRowCount(len(self.getLibrary().getBookCodes()))
        r=0
        for b in self.getLibrary().getBookList():
            self.setItem(r,0,QTableWidgetItem(b.getName()))
            self.setCellWidget(r,1,pixWidget(b.getImg()))
            self.setItem(r,2,QTableWidgetItem(b.getAuthorBiblioStr()))
            if b.getPubl():self.setItem(r,3,QTableWidgetItem(b.getPubl().getName()))
            else:self.setItem(r,3,QTableWidgetItem(''))
            self.setItem(r,4,QTableWidgetItem(str(b.getYear())))
            self.setItem(r,5,QTableWidgetItem(str(b.getPages())))
            self.appendRowCode(r,b.getCode())
            r+=1