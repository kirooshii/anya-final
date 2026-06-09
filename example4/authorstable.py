from PyQt5.QtWidgets import QTableWidgetItem
from dbtablewidget import dbTableWidget

class authorsTable(dbTableWidget):
    def __init__(self,library,parent=None):
        dbTableWidget.__init__(self,library=library,parent=parent,header=[u'фамилия',u'имя',u'отчество'])
    def setData(self):
        self.setRowCount(len(self.getLibrary().getAuthorCodes()))
        r=0
        for a in self.getLibrary().getAuthorList():
            self.setItem(r,0,QTableWidgetItem(a.getSurname()))
            self.setItem(r,1,QTableWidgetItem(a.getName()))
            self.setItem(r,2,QTableWidgetItem(a.getSecname()))
            self.appendRowCode(r,a.getCode())
            r+=1