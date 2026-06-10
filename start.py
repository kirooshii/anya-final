import cherrypy
import sys
import os
from accounting import accounting
from dataxml import dataxml
from departmentpage_web import departmentpage
from expensetypepage_web import expensetypepage
from expensepage_web import expensepage

class start:
    def __init__(self):
        self.__acc=accounting()
        self.__load=False
        self.__fname=''
        self.__dformat=''
        self.__dataxml=dataxml(self.__acc)
        self.departmentpage=departmentpage(self.__acc)
        self.expensetypepage=expensetypepage(self.__acc)
        self.expensepage=expensepage(self.__acc)
    def index(self):
        if not(self.__load):
            s="""<form action=openfile method=post>
            Открыть файл<br>
            <input type=text name=fname value=''>
            <select name=dformat>
            <option value=XML>XML</option>
            </select><br>
            <input type=submit>
            </form>
            """
        else:
            sxml=''
            if self.__dformat=='XML':sxml=' selected'
            s="""
            <a href=departmentpage/>отделы</a><br>
            <a href=expensetypepage/>виды расходов</a><br>
            <a href=expensepage/>расходы</a><br>
            <hr>
            <form action=savefile method=post>
            Сохранить файл<br>
            <input type=text name=fname value=%s>
            <select name=dformat>
            <option%s value=XML>XML</option>
            </select><br>
            <input type=submit>
            </form>
            """%(self.__fname,sxml)
        return s
    index.exposed=True

    def openfile(self, fname='', dformat='', **kwargs):
        if dformat=='XML' and fname:
            self.__dataxml.readFile(filename=fname)
            self.__load=True
            self.__fname=fname
            self.__dformat=dformat
            return "Данные открыты<br><a href=./index>назад</a>"
        return "Ошибка: файл не найден<br><a href=./index>назад</a>"
    openfile.exposed=True

    def savefile(self, fname='', dformat='', **kwargs):
        if dformat=='XML' and fname:
            self.__dataxml.writeFile(filename=fname)
            return "Данные сохранены<br><a href=./index>назад</a>"
        return "Ошибка сохранения<br><a href=./index>назад</a>"
    savefile.exposed=True

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(start(), '/', conf)
