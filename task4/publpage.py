from page import page
from publstable import publsTable
from publeditform import publEditForm

class publPage(page):
    def __init__(self,library,parent=None):
        page.__init__(self,library=library,parent=parent)
        self.setTable(publsTable(library=library,parent=parent))
        self.setForm(publEditForm(library=library,parent=parent))
        self.setConnect()