from PyQt5.QtWidgets import QLineEdit,QDoubleSpinBox,QDateEdit
from PyQt5.QtCore import QDate
from editform import editForm
from departmentcombo import departmentCombo
from expensetypecombo import expensetypeCombo

class expenseEditForm(editForm):
    def __init__(self,parent=None,library=None):
        editForm.__init__(self,library=library,parent=parent)
        self.__expensetypeCombo=expensetypeCombo(library=library)
        self.__departmentCombo=departmentCombo(library=library)
        self.__amountSpin=QDoubleSpinBox()
        self.__amountSpin.setRange(0,10000000)
        self.__dateEdit=QDateEdit()
        self.__dateEdit.setCalendarPopup(True)
        self.__dateEdit.setDate(QDate.currentDate())
        self.addLabel(u'вид расхода',0,0)
        self.addNewWidget(self.__expensetypeCombo,0,1)
        self.addLabel(u'отдел',1,0)
        self.addNewWidget(self.__departmentCombo,1,1)
        self.addLabel(u'сумма',2,0)
        self.addNewWidget(self.__amountSpin,2,1)
        self.addLabel(u'дата',3,0)
        self.addNewWidget(self.__dateEdit,3,1)
        if self.getLibrary().getExpenseList():
            self.setCurrentCode(self.getLibrary().getExpenseList()[0].getCode())
    def update(self):
        if self.getCurrentCode() in self.getLibrary().getExpenseCodes():
            self.__expensetypeCombo.setCurrentRec(self.getCurrentCode())
            self.__departmentCombo.setCurrentRec(self.getCurrentCode())
            self.__amountSpin.setValue(self.getLibrary().getExpense(self.getCurrentCode()).getAmount())
            if self.getLibrary().getExpense(self.getCurrentCode()).getDate():
                self.__dateEdit.setDate(QDate.fromString(self.getLibrary().getExpense(self.getCurrentCode()).getDate(),'yyyy-MM-dd'))
    def editClick(self):
        self.getLibrary().getExpense(self.getCurrentCode()).setExpenseType(self.getLibrary().getExpenseType(self.__expensetypeCombo.getCurrentCode()))
        self.getLibrary().getExpense(self.getCurrentCode()).setDepartment(self.getLibrary().getDepartment(self.__departmentCombo.getCurrentCode()))
        self.getLibrary().getExpense(self.getCurrentCode()).setAmount(self.__amountSpin.value())
        self.getLibrary().getExpense(self.getCurrentCode()).setDate(self.__dateEdit.date().toString('yyyy-MM-dd'))
    def newClick(self):
        e=self.getLibrary().newExpense("",None,None,0,'')
        self.setCurrentCode(e.getCode())
    def delClick(self):
        self.getLibrary().removeExpense(self.getCurrentCode())
