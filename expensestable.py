from PyQt5.QtWidgets import QTableWidgetItem
from dbtablewidget import dbTableWidget

class expensesTable(dbTableWidget):
    def __init__(self,library,parent=None):
        dbTableWidget.__init__(self,library=library,parent=parent,header=[u'вид расхода',u'отдел',u'сумма',u'дата'])
    def setData(self):
        self.setRowCount(len(self.getLibrary().getExpenseCodes()))
        r=0
        for e in self.getLibrary().getExpenseList():
            self.setItem(r,0,QTableWidgetItem(e.getExpenseTypeName()))
            self.setItem(r,1,QTableWidgetItem(e.getDepartmentName()))
            self.setItem(r,2,QTableWidgetItem(str(e.getAmount())))
            self.setItem(r,3,QTableWidgetItem(e.getDate()))
            self.appendRowCode(r,e.getCode())
            r+=1
