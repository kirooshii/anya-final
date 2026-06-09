from generallist import generalList
from author import author

class authorList(generalList):
    def appendItem(self,value):
        if isinstance(value,author):generalList.appendItem(self,value)
    def createItem(self,code,surname,name='',secname=''):
        if code in self.getCodes():print('Автор с кодом %s уже существует'%(code,))
        else:
            a=author(code,surname,name,secname)
            self.appendItem(a)
            return a
    def newItem(self,surname,name='',secname=''):
        a=author(self.getNewCode(),surname,name,secname)
        self.appendItem(a)
        return a
    def getBiblioStr(self):
        s=''
        for i in self.getItems():
            s+=i.getBiblioStr()+', '
        if s:s=s[:-2]
        return s