from expensetype import expensetype
from generallist import generalList

class expensetypeList(generalList):
    def appendItem(self,value):
        if isinstance(value,expensetype):generalList.appendItem(self,value)
    def createItem(self,code,name,description='',limit=0):
        if code in self.getCodes():print('Вид расхода с кодом %s уже существует'%(code,))
        else:
            e=expensetype(code,name,description,limit)
            self.appendItem(e)
            return e
    def newItem(self,name,description='',limit=0):
        e=expensetype(self.getNewCode(),name,description,limit)
        self.appendItem(e)
        return e
