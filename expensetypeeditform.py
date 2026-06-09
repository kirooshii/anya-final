from PyQt5.QtWidgets import QLineEdit,QDoubleSpinBox
from editform import editForm

class expensetypeEditForm(editForm):
    def __init__(self,parent=None,library=None):
        editForm.__init__(self,library=library,parent=parent)
        self.__nameEdit=QLineEdit()
        self.__descriptionEdit=QLineEdit()
        self.__limitSpin=QDoubleSpinBox()
        self.__limitSpin.setRange(0,10000000)
        self.addLabel(u'название',0,0)
        self.addNewWidget(self.__nameEdit,0,1)
        self.addLabel(u'описание',1,0)
        self.addNewWidget(self.__descriptionEdit,1,1)
        self.addLabel(u'предельная норма',2,0)
        self.addNewWidget(self.__limitSpin,2,1)
        if self.getLibrary().getExpenseTypeList():
            self.setCurrentCode(self.getLibrary().getExpenseTypeList()[0].getCode())
    def update(self):
        if self.getCurrentCode() in self.getLibrary().getExpenseTypeCodes():
            self.__nameEdit.setText(self.getLibrary().getExpenseType(self.getCurrentCode()).getName())
            self.__descriptionEdit.setText(self.getLibrary().getExpenseType(self.getCurrentCode()).getDescription())
            self.__limitSpin.setValue(self.getLibrary().getExpenseType(self.getCurrentCode()).getLimit())
    def editClick(self):
        self.getLibrary().getExpenseType(self.getCurrentCode()).setName(self.__nameEdit.text())
        self.getLibrary().getExpenseType(self.getCurrentCode()).setDescription(self.__descriptionEdit.text())
        self.getLibrary().getExpenseType(self.getCurrentCode()).setLimit(self.__limitSpin.value())
    def newClick(self):
        e=self.getLibrary().newExpenseType("","",0)
        self.setCurrentCode(e.getCode())
    def delClick(self):
        self.getLibrary().removeExpenseType(self.getCurrentCode())
