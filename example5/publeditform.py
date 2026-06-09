from PyQt5.QtWidgets import QLineEdit
from editform import editForm

class publEditForm(editForm):
    def __init__(self,parent=None,library=None):
        editForm.__init__(self,library=library,parent=parent)
        self.__nameEdit=QLineEdit()
        self.__shortnameEdit=QLineEdit()
        self.addLabel(u'название',0,0)
        self.addNewWidget(self.__nameEdit,0,1)
        self.addLabel(u'сокр. название',1,0)
        self.addNewWidget(self.__shortnameEdit,1,1)
        if self.getLibrary().getPublList():
            self.setCurrentCode(self.getLibrary().getPublList()[0].getCode())
    def update(self):
        if self.getCurrentCode() in self.getLibrary().getPublCodes():
            self.__nameEdit.setText(self.getLibrary().getPubl(self.getCurrentCode()).getName())
            self.__shortnameEdit.setText(self.getLibrary().getPubl(self.getCurrentCode()).getShortname())
    def editClick(self):
        self.getLibrary().getPubl(self.getCurrentCode()).setName(self.__nameEdit.text())
        self.getLibrary().getPubl(self.getCurrentCode()).setShortname(self.__shortnameEdit.text())
    def newClick(self):
        p=self.getLibrary().newPubl("","")
        self.setCurrentCode(p.getCode())
    def delClick(self):
        self.getLibrary().removePubl(self.getCurrentCode())