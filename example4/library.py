from authorlist import authorList
from publlist import publList
from booklist import bookList

class library:
    def __init__(self):
        self.__authorList=authorList()
        self.__publList=publList()
        self.__bookList=bookList()
    def clear(self):
        self.__bookList.clear()
        self.__authorList.clear()
        self.__publList.clear()
    def createAuthor(self,code,surname,name='',secname=''):return self.__authorList.createItem(code,surname,name,secname)
    def newAuthor(self,surname,name='',secname=''):return self.__authorList.newItem(surname,name,secname)
    def removeAuthor(self,value):
        self.__authorList.removeItem(value)
        for b in self.__bookList.getItems():
            b.removeAuthor(value)
    def getAuthor(self,code):return self.__authorList.findByCode(code)
    def getAuthorList(self):return self.__authorList.getItems()
    def getAuthorCodes(self):return self.__authorList.getCodes()
    def getAuthorNewCode(self):return self.__authorList.getNewCode()

    def createPubl(self,code,name,shortname=''):return self.__publList.createItem(code,name,shortname)
    def newPubl(self,name,shortname=''):return self.__publList.newItem(name,shortname)
    def removePubl(self,code):
        self.__publList.removeItem(code)
        for b in self.__bookList.getItems():
            if b.getPublCode()==code:b.setPubl(None)
    def getPubl(self,code):return self.__publList.findByCode(code)
    def getPublList(self):return self.__publList.getItems()
    def getPublCodes(self):return self.__publList.getCodes()
    def getPublNewCode(self):return self.__publList().getNewCode()

    def createBook(self,code,name,img='',publ=None,year=0,pages=0):
        return self.__bookList.createItem(code,name,img,publ,year,pages)
    def newBook(self,name,img='',publ=None,year=0,pages=0):
        return self.__bookList.newItem(name,img,publ,year,pages)
    def removeBook(self,code):self.__bookList.removeItem(code)
    def getBook(self,code):return self.__bookList.findByCode(code)
    def getBookList(self):return self.__bookList.getItems()
    def getBookCodes(self):return self.__bookList.getCodes()
    def getBookNewCode(self):return self.__bookList().getNewCode()