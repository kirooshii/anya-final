from departmentlist import departmentList
from expensetypelist import expensetypeList
from expenselist import expenseList

class accounting:
    def __init__(self):
        self.__departmentList=departmentList()
        self.__expensetypeList=expensetypeList()
        self.__expenseList=expenseList()
    def clear(self):
        self.__expenseList.clear()
        self.__departmentList.clear()
        self.__expensetypeList.clear()
    def createDepartment(self,code,name,employees=0):return self.__departmentList.createItem(code,name,employees)
    def newDepartment(self,name,employees=0):return self.__departmentList.newItem(name,employees)
    def removeDepartment(self,code):
        self.__departmentList.removeItem(code)
        for e in self.__expenseList.getItems():
            if e.getDepartmentCode()==code:e.setDepartment(None)
    def getDepartment(self,code):return self.__departmentList.findByCode(code)
    def getDepartmentList(self):return self.__departmentList.getItems()
    def getDepartmentCodes(self):return self.__departmentList.getCodes()
    def getDepartmentNewCode(self):return self.__departmentList.getNewCode()

    def createExpenseType(self,code,name,description='',limit=0):return self.__expensetypeList.createItem(code,name,description,limit)
    def newExpenseType(self,name,description='',limit=0):return self.__expensetypeList.newItem(name,description,limit)
    def removeExpenseType(self,code):
        self.__expensetypeList.removeItem(code)
        for e in self.__expenseList.getItems():
            if e.getExpenseTypeCode()==code:e.setExpenseType(None)
    def getExpenseType(self,code):return self.__expensetypeList.findByCode(code)
    def getExpenseTypeList(self):return self.__expensetypeList.getItems()
    def getExpenseTypeCodes(self):return self.__expensetypeList.getCodes()
    def getExpenseTypeNewCode(self):return self.__expensetypeList.getNewCode()

    def createExpense(self,code,name='',expensetype=None,department=None,amount=0,date=''):
        return self.__expenseList.createItem(code,name,expensetype,department,amount,date)
    def newExpense(self,name='',expensetype=None,department=None,amount=0,date=''):
        return self.__expenseList.newItem(name,expensetype,department,amount,date)
    def removeExpense(self,code):self.__expenseList.removeItem(code)
    def getExpense(self,code):return self.__expenseList.findByCode(code)
    def getExpenseList(self):return self.__expenseList.getItems()
    def getExpenseCodes(self):return self.__expenseList.getCodes()
    def getExpenseNewCode(self):return self.__expenseList.getNewCode()
