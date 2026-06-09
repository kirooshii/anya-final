from dblistwidget import dbListWidget

class authorListWidget(dbListWidget):
    def update(self):
        self.clear()
        l=self.getLibrary().getBook(self.getCurrentRec()).getAuthorList()
        for a in l:
            self.addItem(a.getCode(),a.getBiblioStr())
        if l:self.setCurrentRow(0)