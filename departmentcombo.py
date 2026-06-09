from dbcombobox import dbComboBox

class departmentCombo(dbComboBox):
    def update(self):
        self.clear()
        for d in self.getLibrary().getDepartmentList():
            self.addItem(d.getCode(),d.getName())
        if self.getCurrentRec() in self.getLibrary().getExpenseCodes():
            if self.getLibrary().getExpense(self.getCurrentRec()).getDepartment():
                self.setCurrentCode(self.getLibrary().getExpense(self.getCurrentRec()).getDepartment().getCode())
