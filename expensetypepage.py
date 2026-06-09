from page import page
from expensetypestable import expensetypesTable
from expensetypeeditform import expensetypeEditForm

class expensetypePage(page):
    def __init__(self,library,parent=None):
        page.__init__(self,library=library,parent=parent)
        self.setTable(expensetypesTable(library=library,parent=parent))
        self.setForm(expensetypeEditForm(library=library,parent=parent))
        self.setConnect()
