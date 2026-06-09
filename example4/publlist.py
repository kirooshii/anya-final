from publ import publ
from generallist import generalList

class publList(generalList):
    def appendItem(self,value):
        if isinstance(value,publ):generalList.appendItem(self,value)
    def newItem(self,name,shortname=''):
        p=publ(self.getNewCode(),name,shortname)
        self.appendItem(p)
        return p
    def createItem(self,code,name,shortname=''):
        if code in self.getCodes():print('Издательство с кодом %s уже существует'%(code,))
        else:
            p=publ(code,name,shortname)
            self.appendItem(p)
            return p