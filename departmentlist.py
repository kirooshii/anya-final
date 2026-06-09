from department import department
from generallist import generalList

class departmentList(generalList):
    def appendItem(self,value):
        if isinstance(value,department):generalList.appendItem(self,value)
    def createItem(self,code,name,employees=0):
        if code in self.getCodes():print('Отдел с кодом %s уже существует'%(code,))
        else:
            d=department(code,name,employees)
            self.appendItem(d)
            return d
    def newItem(self,name,employees=0):
        d=department(self.getNewCode(),name,employees)
        self.appendItem(d)
        return d
