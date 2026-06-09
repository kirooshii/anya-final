from dbcombobox import dbComboBox

class publCombo(dbComboBox):
    def update(self):
        self.clear()
        for p in self.getLibrary().getPublList():
            self.addItem(p.getCode(),p.getName())
        if self.getLibrary().getBook(self.getCurrentRec()).getPubl():
            self.setCurrentCode(self.getLibrary().getBook(self.getCurrentRec()).getPubl().getCode())