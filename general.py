class general:
    def __init__(self,code=0,name=''):
        self.setCode(code)
        self.setName(name)
    def setCode(self,value):self.__code=value
    def setName(self,value):self.__name=value
    def getCode(self):return self.__code
    def getName(self):return self.__name
