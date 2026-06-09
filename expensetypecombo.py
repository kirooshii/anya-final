from dbcombobox import dbComboBox

class expensetypeCombo(dbComboBox):
    def update(self):
        self.clear()
        for e in self.getLibrary().getExpenseTypeList():
            self.addItem(e.getCode(),e.getName())
        if self.getCurrentRec() in self.getLibrary().getExpenseCodes():
            if self.getLibrary().getExpense(self.getCurrentRec()).getExpenseType():
                self.setCurrentCode(self.getLibrary().getExpense(self.getCurrentRec()).getExpenseType().getCode())
