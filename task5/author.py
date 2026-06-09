from general import general

class author(general):
    def __init__(self,code=0,surname='',name='',secname=''):
        general.__init__(self,code,name)
        self.setSurname(surname)
        self.setSecname(secname)
    def setSurname(self,value):self.__surname=value
    def setSecname(self,value):self.__secname=value
    def getSurname(self):return self.__surname
    def getSecname(self):return self.__secname
    def getShortname(self):
        if self.getName():return self.getName()[0]
        else:return ''
    def getShortsecname(self):
        if self.getSecname():return self.getSecname()[0]
        else:return ''
    def getBiblioStr(self):
        s=self.getSurname()
        if self.getShortname():s+=' %s.'%(self.getShortname(),)
        if self.getShortsecname():s+=' %s.'%(self.getShortsecname(),)
        return s