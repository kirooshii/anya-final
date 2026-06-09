from page import page
from bookstable import booksTable
from bookeditform import bookEditForm

class bookPage(page):
    def __init__(self,library,parent=None):
        page.__init__(self,library=library,parent=parent)
        self.setTable(booksTable(library=library,parent=parent))
        self.setForm(bookEditForm(library=library,parent=parent))
        self.setConnect()