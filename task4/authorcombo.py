from dbcombobox import dbComboBox

class authorCombo(dbComboBox):
    def update(self):
        self.clear()
        for a in self.getLibrary().getAuthorList():
            if not(a in self.getLibrary().getBook(self.getCurrentRec()).getAuthorList()):
                self.addItem(a.getCode(),a.getBiblioStr())