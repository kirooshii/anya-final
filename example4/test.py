from PyQt5.QtWidgets import QApplication
from library import library
from dataxml import dataxml
from bookstable import booksTable
import sys

app = QApplication(sys.argv)
lib=library()
dat1=dataxml(lib,'old.xml')
dat1.read()
tw1=booksTable(library=lib)
tw1.show()
sys.exit(app.exec_())

