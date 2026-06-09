from expense import expense
from generallist import generalList

class expenseList(generalList):
    def appendItem(self,value):
        if isinstance(value,expense):generalList.appendItem(self,value)
    def createItem(self,code,name='',expensetype=None,department=None,amount=0,date=''):
        if code in self.getCodes():print('Расход с кодом %s уже существует'%(code,))
        else:
            e=expense(code,name,expensetype,department,amount,date)
            self.appendItem(e)
            return e
    def newItem(self,name='',expensetype=None,department=None,amount=0,date=''):
        e=expense(self.getNewCode(),name,expensetype,department,amount,date)
        self.appendItem(e)
        return e
