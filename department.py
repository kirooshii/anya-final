from general import general

class department(general):
    def __init__(self,code=0,name='',employees=0):
        general.__init__(self,code,name)
        self.setEmployees(employees)
    def setEmployees(self,value):self.__employees=value
    def getEmployees(self):return self.__employees
