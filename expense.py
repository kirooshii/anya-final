from general import general
from department import department
from expensetype import expensetype

class expense(general):
    def __init__(self,code=0,name='',expensetype=None,department=None,amount=0,date=''):
        general.__init__(self,code,name)
        self.setExpenseType(expensetype)
        self.setDepartment(department)
        self.setAmount(amount)
        self.setDate(date)
    def setExpenseType(self,value):self.__expensetype=value
    def setDepartment(self,value):self.__department=value
    def setAmount(self,value):self.__amount=value
    def setDate(self,value):self.__date=value
    def getExpenseType(self):return self.__expensetype
    def getExpenseTypeCode(self):
        if self.getExpenseType():return self.getExpenseType().getCode()
        else:return 0
    def getExpenseTypeName(self):
        if self.getExpenseType():return self.getExpenseType().getName()
        else:return ''
    def getDepartment(self):return self.__department
    def getDepartmentCode(self):
        if self.getDepartment():return self.getDepartment().getCode()
        else:return 0
    def getDepartmentName(self):
        if self.getDepartment():return self.getDepartment().getName()
        else:return ''
    def getAmount(self):return self.__amount
    def getDate(self):return self.__date
