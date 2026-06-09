from PyQt5.QtWidgets import QTableWidgetItem
from dbtablewidget import dbTableWidget

class expensetypesTable(dbTableWidget):
    def __init__(self,library,parent=None):
        dbTableWidget.__init__(self,library=library,parent=parent,header=[u'название',u'описание',u'предельная норма'])
    def setData(self):
        self.setRowCount(len(self.getLibrary().getExpenseTypeCodes()))
        r=0
        for e in self.getLibrary().getExpenseTypeList():
            self.setItem(r,0,QTableWidgetItem(e.getName()))
            self.setItem(r,1,QTableWidgetItem(e.getDescription()))
            self.setItem(r,2,QTableWidgetItem(str(e.getLimit())))
            self.appendRowCode(r,e.getCode())
            r+=1
