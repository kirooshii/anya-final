from PyQt5.QtWidgets import QTableWidgetItem
from dbtablewidget import dbTableWidget

class departmentsTable(dbTableWidget):
    def __init__(self,library,parent=None):
        dbTableWidget.__init__(self,library=library,parent=parent,header=[u'название',u'количество сотрудников'])
    def setData(self):
        self.setRowCount(len(self.getLibrary().getDepartmentCodes()))
        r=0
        for d in self.getLibrary().getDepartmentList():
            self.setItem(r,0,QTableWidgetItem(d.getName()))
            self.setItem(r,1,QTableWidgetItem(str(d.getEmployees())))
            self.appendRowCode(r,d.getCode())
            r+=1
