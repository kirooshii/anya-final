from general import general
from publ import publ
from authorlist import authorList

class book(general):
    def __init__(self,code=0,name='',img='',publ=None,year=0,pages=0):
        general.__init__(self,code,name)
        self.__authorList=authorList()
        self.setImg(img)
        self.setPubl(publ)
        self.setPages(pages)
        self.setYear(year)
    def setImg(self,value):self.__img=value
    def setPubl(self,value):self.__publ=value
    def setPages(self,value):self.__pages=value
    def setYear(self,value):self.__year=value
    def getImg(self):return self.__img
    def getPubl(self):return self.__publ
    def getPublCode(self):
        if self.getPubl():return self.getPubl().getCode()
        else: return 0
    def getPublName(self):
        if self.getPubl():return self.getPubl().getName()
        else: return ''
    def getPublShortname(self):
        if self.getPubl():return self.getPubl().getShortname()
        else: return ''
    def getPages(self):return self.__pages
    def getYear(self):return self.__year
    def appendAuthor(self,value):self.__authorList.appendItem(value)
    def removeAuthor(self,value):self.__authorList.removeItem(value)
    def clearAuthorList(self):self.__authorList.clear()
    def getAuthor(self,code):return self.__authorList.findByCode(code)
    def getAuthorList(self):return self.__authorList.getItems()
    def getAuthorCodes(self):return self.__authorList.getCodes()
    def getAuthorBiblioStr(self):return self.__authorList.getBiblioStr()
    def getBiblioStr(self):
        s=self.getAuthorBiblioStr()
        s+=' %s - %s, %s. - %s c.'%(self.getName(), self.getPublShortname(), str(self.getYear()), str(self.getPages()))
        return s