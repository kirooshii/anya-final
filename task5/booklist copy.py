from book import book
from generallist import generalList

class bookList(generalList):
    def appendItem(self,value):
        if isinstance(value,book):generalList.appendItem(self,value)
    def createItem(self,code,name,img='',publ=None,year=0,pages=0):
        if code in self.getCodes():print('Книга с кодом %s уже существует'%(code,))
        else:
            b=book(code,name,img,publ,year,pages)
            self.appendItem(b)
            return b
    def newItem(self,name,img='',publ=None,year=0,pages=0):
        b=book(self.getNewCode(),name,img,publ,year,pages)
        self.appendItem(b)
        return b