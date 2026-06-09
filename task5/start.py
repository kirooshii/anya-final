import cherrypy
import sys
import os
sys.path.insert(0, "./library")
from library import library
from dataxml import dataxml
from bookpage import bookpage

class start:
    def __init__(self):
        self.__lib=library()
        self.__load=False
        self.__fname=''
        self.__dformat=''
        self.__dataxml=dataxml(self.__lib)
        self.bookpage=bookpage(self.__lib)
    def index(self):
        if not(self.__load):
            s="""<form action=openfile metod=post>
            Открыть файл<br>
            <input type=text name=fname value=''>
            <select name=dformat>
            <option value=XML>XML</option>
            <option value=JSON>JSON</option>
            <option value=SQL>SQL</option>
            </select><br>
            <input type=submit>
            </form>
            """
        else:
            sxml,sjson,ssql='','',''
            if self.__dformat=='XML':sxml=' selected'
            elif self.__dformat=='JSON':sjson=' selected'
            elif self.__dformat=='SQL':ssql=' selected'
            s="""
            <a href=bookpage\>книги</a><br>
            <a href=authorpage\>авторы</a><br>
            <a href=publpage\>издательства</a><br>
            <hr>
            <form action=savefile metod=post>
            Сохранить файл<br>
            <input type=text name=fname value=%s>
            <select name=dformat>
            <option%s value=XML>XML</option>
            <option%s value=JSON>JSON</option>
            <option%s value=SQL>SQL</option>
            </select><br>
            <input type=submit>
            </form>
            """%(self.__fname,sxml,sjson,ssql)
        return s
    index.exposed=True

    def openfile(self,fname='',dformat=''):
        # Убрали try:
        if dformat=='XML':self.__dataxml.readFile(fname)
        elif dformat=='JSON':self.__datajson.readFile(fname)
        elif dformat=='SQL':self.__datasql.readFile(fname)
        self.__load=True
        self.__fname=fname
        self.__dformat=dformat
        return "Данные открыты<br><a href=./index>назад</a>"
        # Убрали except: ...

    def savefile(self,fname='',dformat=''):
        if dformat=='XML':self.__dataxml.writeFile(fname)
        elif dformat=='JSON':self.__datajson.writeFile(fname)
        elif dformat=='SQL':
            if os.path.isfile(fname):os.remove(fname)
            self.__datasql.writeFile(fname)
        return "Данные сохранены<br><a href=./index>назад</a>"
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