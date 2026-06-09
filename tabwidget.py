from PyQt5.QtWidgets import QTabWidget
from departmentpage import departmentPage
from expensetypepage import expensetypePage
from expensepage import expensePage

class tabWidget(QTabWidget):
    def __init__(self,accounting,parent=None):
        QTabWidget.__init__(self,parent)
        self.__departmentPage=departmentPage(library=accounting)
        self.addTab(self.__departmentPage,u"отделы")
        self.__expensetypePage=expensetypePage(library=accounting)
        self.addTab(self.__expensetypePage,u"виды расходов")
        self.__expensePage=expensePage(library=accounting)
        self.addTab(self.__expensePage,u"расходы")
        self.currentChanged.connect(self.update)
    def update(self):
        self.__departmentPage.update()
        self.__expensetypePage.update()
        self.__expensePage.update()
