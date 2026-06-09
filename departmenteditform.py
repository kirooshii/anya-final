from PyQt5.QtWidgets import QLineEdit,QSpinBox
from editform import editForm

class departmentEditForm(editForm):
    def __init__(self,parent=None,library=None):
        editForm.__init__(self,library=library,parent=parent)
        self.__nameEdit=QLineEdit()
        self.__employeesSpin=QSpinBox()
        self.__employeesSpin.setRange(0,100000)
        self.addLabel(u'название',0,0)
        self.addNewWidget(self.__nameEdit,0,1)
        self.addLabel(u'количество сотрудников',1,0)
        self.addNewWidget(self.__employeesSpin,1,1)
        if self.getLibrary().getDepartmentList():
            self.setCurrentCode(self.getLibrary().getDepartmentList()[0].getCode())
    def update(self):
        if self.getCurrentCode() in self.getLibrary().getDepartmentCodes():
            self.__nameEdit.setText(self.getLibrary().getDepartment(self.getCurrentCode()).getName())
            self.__employeesSpin.setValue(self.getLibrary().getDepartment(self.getCurrentCode()).getEmployees())
    def editClick(self):
        self.getLibrary().getDepartment(self.getCurrentCode()).setName(self.__nameEdit.text())
        self.getLibrary().getDepartment(self.getCurrentCode()).setEmployees(self.__employeesSpin.value())
    def newClick(self):
        d=self.getLibrary().newDepartment("",0)
        self.setCurrentCode(d.getCode())
    def delClick(self):
        self.getLibrary().removeDepartment(self.getCurrentCode())
