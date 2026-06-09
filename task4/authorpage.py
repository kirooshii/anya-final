from page import page
from authorstable import authorsTable
from authoreditform import authorEditForm

class authorPage(page):
    def __init__(self,library,parent=None):
        page.__init__(self,library=library,parent=parent)
        self.setTable(authorsTable(library=library,parent=parent))
        self.setForm(authorEditForm(library=library,parent=parent))
        self.setConnect()