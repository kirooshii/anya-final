from PyQt5.QtWidgets import QTableWidgetItem
from dbtablewidget import dbTableWidget

class publsTable(dbTableWidget):
    def __init__(self,library,parent=None):
        dbTableWidget.__init__(self,library=library,parent=parent,header=[u'название',u'сокр. название'])
    def setData(self):
        self.setRowCount(len(self.getLibrary().getPublCodes()))
        r=0
        for p in self.getLibrary().getPublList():
            self.setItem(r,0,QTableWidgetItem(p.getName()))
            self.setItem(r,1,QTableWidgetItem(p.getShortname()))
            self.appendRowCode(r,p.getCode())
            r+=1