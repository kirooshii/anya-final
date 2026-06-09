from general import general

class expensetype(general):
    def __init__(self,code=0,name='',description='',limit=0):
        general.__init__(self,code,name)
        self.setDescription(description)
        self.setLimit(limit)
    def setDescription(self,value):self.__description=value
    def setLimit(self,value):self.__limit=value
    def getDescription(self):return self.__description
    def getLimit(self):return self.__limit
