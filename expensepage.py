from page import page
from expensestable import expensesTable
from expenseeditform import expenseEditForm

class expensePage(page):
    def __init__(self,library,parent=None):
        page.__init__(self,library=library,parent=parent)
        self.setTable(expensesTable(library=library,parent=parent))
        self.setForm(expenseEditForm(library=library,parent=parent))
        self.setConnect()
