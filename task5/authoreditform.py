from PyQt5.QtWidgets import QLineEdit
from editform import editForm

class authorEditForm(editForm):
    def __init__(self,parent=None,library=None):
        editForm.__init__(self,library=library,parent=parent)
        self.__surnameEdit=QLineEdit()
        self.__nameEdit=QLineEdit()
        self.__secnameEdit=QLineEdit()
        self.addLabel(u'фамилия',0,0)
        self.addNewWidget(self.__surnameEdit,0,1)
        self.addLabel(u'имя',1,0)
        self.addNewWidget(self.__nameEdit,1,1)
        self.addLabel(u'отчество',2,0)
        self.addNewWidget(self.__secnameEdit,2,1)
        if self.getLibrary().getAuthorList():
            self.setCurrentCode(self.getLibrary().getAuthorList()[0].getCode())
    def update(self):
        if self.getCurrentCode() in self.getLibrary().getAuthorCodes():
            self.__surnameEdit.setText(self.getLibrary().getAuthor(self.getCurrentCode()).getSurname())
            self.__nameEdit.setText(self.getLibrary().getAuthor(self.getCurrentCode()).getName())
            self.__secnameEdit.setText(self.getLibrary().getAuthor(self.getCurrentCode()).getSecname())
    def editClick(self):
        self.getLibrary().getAuthor(self.getCurrentCode()).setSurname(self.__surnameEdit.text())
        self.getLibrary().getAuthor(self.getCurrentCode()).setName(self.__nameEdit.text())
        self.getLibrary().getAuthor(self.getCurrentCode()).setSecname(self.__secnameEdit.text())
    def newClick(self):
        a=self.getLibrary().newAuthor("","","")
        self.setCurrentCode(a.getCode())
    def delClick(self):
        self.getLibrary().removeAuthor(self.getCurrentCode())