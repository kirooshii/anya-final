from PyQt5.QtWidgets import QVBoxLayout,QLineEdit,QPushButton,QLabel,QSpinBox,QFileDialog
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from editform import editForm
from dblistwidget import dbListWidget
from dbcombobox import dbComboBox
from publcombo import publCombo
from authorcombo import authorCombo
from authorlistwidget import authorListWidget

class bookEditForm(editForm):
    def __init__(self,parent=None,library=None):
        editForm.__init__(self,library=library,parent=parent)
        self.__pixlabel=QLabel()
        self.__nameEdit=QLineEdit()
        self.__imgEdit=QLineEdit()
        self.__imgButton=QPushButton(u'выбор')
        self.__authorListWidget=authorListWidget(library=library)
        self.__removeButton=QPushButton(u'удалить')
        self.__authorCombo=authorCombo(library=library)
        self.__appendButton=QPushButton(u'добавить')
        self.__publCombo=publCombo(library=library)
        self.__yearSpin=QSpinBox()
        self.__yearSpin.setRange(-3000,QtCore.QDate().currentDate().year())
        self.__pagesSpin=QSpinBox()
        self.__pagesSpin.setRange(0,10000)
        self.addLabel('название',0,0)
        self.addNewWidget(self.__nameEdit,0,1)
        self.addLabel(u'обложка',1,0)
        self.addNewWidget(self.__imgEdit,1,1)
        self.addNewWidget(self.__imgButton,1,2)
        self.addLabel(u'авторы',2,0)
        self.addNewWidget(self.__authorListWidget,2,1)
        self.addNewWidget(self.__removeButton,2,2)
        self.addNewWidget(self.__authorCombo,3,1)
        self.addNewWidget(self.__appendButton,3,2)
        self.addLabel(u'издательство',4,0)
        self.addNewWidget(self.__publCombo,4,1)
        self.addLabel(u'год',5,0)
        self.addNewWidget(self.__yearSpin,5,1)
        self.addLabel(u'страницы',6,0)
        self.addNewWidget(self.__pagesSpin,6,1)
        self.__pixVBox=QVBoxLayout()
        self.__pixVBox.addWidget(self.__pixlabel)
        self.__pixVBox.addStretch(1)
        self.addLeftLayout(self.__pixVBox)
        self.__removeButton.clicked.connect(self.removeAuthor)
        self.__appendButton.clicked.connect(self.appendAuthor)
        self.__imgButton.clicked.connect(self.openImg)
        if self.getLibrary().getBookList():
            self.setCurrentCode(self.getLibrary().getBookList()[0].getCode())
    def openImg(self):
        filename=QFileDialog.getOpenFileName(self, 'Open file', './')[0]
        if filename:
            self.__imgEdit.setText(filename)
            self.__pixlabel.setPixmap(QPixmap(filename))
    def update(self):
        if self.getCurrentCode() in self.getLibrary().getBookCodes():
            self.__nameEdit.setText(self.getLibrary().getBook(self.getCurrentCode()).getName())
            self.__imgEdit.setText(self.getLibrary().getBook(self.getCurrentCode()).getImg())
            self.__pixlabel.setPixmap(QPixmap(self.getLibrary().getBook(self.getCurrentCode()).getImg()))
            self.__publCombo.setCurrentRec(self.getCurrentCode())
            self.__authorListWidget.setCurrentRec(self.getCurrentCode())
            self.__authorCombo.setCurrentRec(self.getCurrentCode())
            self.__yearSpin.setValue(self.getLibrary().getBook(self.getCurrentCode()).getYear())
            self.__pagesSpin.setValue(self.getLibrary().getBook(self.getCurrentCode()).getPages())
    def removeAuthor(self):
        code=self.__authorListWidget.getCurrentCode()
        if code:
            self.__authorListWidget.removeSelected()
            self.__authorCombo.addItem(code,self.getLibrary().getAuthor(code).getBiblioStr())
    def appendAuthor(self):
        code=self.__authorCombo.getCurrentCode()
        if code:
            self.__authorCombo.removeItem(self.__authorCombo.currentIndex())
            self.__authorListWidget.addItem(code,self.getLibrary().getAuthor(code).getBiblioStr())
    def editClick(self):
        self.getLibrary().getBook(self.getCurrentCode()).setName(self.__nameEdit.text())
        self.getLibrary().getBook(self.getCurrentCode()).setImg(self.__imgEdit.text())
        self.getLibrary().getBook(self.getCurrentCode()).clearAuthorList()
        for c in self.__authorListWidget.getCodes():
            self.getLibrary().getBook(self.getCurrentCode()).appendAuthor(self.getLibrary().getAuthor(c))
        self.getLibrary().getBook(self.getCurrentCode()).setPubl(self.getLibrary().getPubl(self.__publCombo.getCurrentCode()))
        self.getLibrary().getBook(self.getCurrentCode()).setYear(self.__yearSpin.value())
        self.getLibrary().getBook(self.getCurrentCode()).setPages(self.__pagesSpin.value())
    def newClick(self):
        b=self.getLibrary().newBook("","",None,0,0)
        self.setCurrentCode(b.getCode())
    def delClick(self):
        self.getLibrary().removeBook(self.getCurrentCode())