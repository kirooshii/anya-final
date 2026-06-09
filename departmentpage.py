from page import page
from departmentstable import departmentsTable
from departmenteditform import departmentEditForm

class departmentPage(page):
    def __init__(self,library,parent=None):
        page.__init__(self,library=library,parent=parent)
        self.setTable(departmentsTable(library=library,parent=parent))
        self.setForm(departmentEditForm(library=library,parent=parent))
        self.setConnect()
