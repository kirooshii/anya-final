from general import general

class generalList:
    def __init__(self):self.__list=[]
    def clear(self):self.__list=[]
    def findByCode(self,code):
        for l in self.__list:
            if l.getCode()==code:
                return l
    def getNewCode(self):
        l=self.getCodes()
        if l:return max(l)+1
        else:return 1
    def getCodes(self):return [s.getCode() for s in self.__list]
    def getItems(self):return [s for s in self.__list]
    def appendItem(self,value):
        self.__list.append(value)
    def removeItem(self,value):
        if isinstance(value,general):self.__list.remove(value)
        if isinstance(value,int):self.__list.remove(self.findByCode(value))