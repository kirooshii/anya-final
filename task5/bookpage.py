class bookpage:
    def __init__(self,library):
        self.__lib=library

    def index(self):
        s='''<a href=..>назад</a>/<a href=addform>добавить</a>
        <table><th bgcolor=gray></th>
        <th bgcolor=gray>название</th>
        <th bgcolor=gray>обложка</th>
        <th bgcolor=gray>авторы</th>
        <th bgcolor=gray>издательство</th>
        <th bgcolor=gray>год</th>
        <th bgcolor=gray>страницы</th>'''
        r=1
        bg=''
        for c in self.__lib.getBookCodes():
            s+='<tr%s><td>%d</td>'%(bg,r)
            s+='<td>%s</td>'%self.__lib.getBook(c).getName()
            s+='<td>%s</td>'%"<a href=imgview?img=%s>%s</a>"%(self.__lib.getBook(c).getImg(),self.__lib.getBook(c).getImg())
            s+='<td>%s</td>'%self.__lib.getBook(c).getAuthorBiblioStr()
            s+='<td>%s</td>'%self.__lib.getBook(c).getPublName()
            s+='<td>%s</td>'%self.__lib.getBook(c).getYear()
            s+='<td>%s</td>'%self.__lib.getBook(c).getPages()
            s+='<td><a href=editform?code=%s>редактировать</a></td>'%c
            s+='<td><a href=delr?code=%s>удалить</a></td></tr>'%c
            r+=1
            if bg:bg=''
            else:bg=' bgcolor=silver'
        s+='</table>'
        return s
    index.exposed=True

    def imgview(self,img):
        return '<img src=../static/img/%s><br><a href=.\>назад</a>'%img
    imgview.exposed=True

    def publCombo(self,code=0):
        s='<select name=publ>'
        for c in self.__lib.getPublCodes():
            if (code in self.__lib.getBookCodes())and(c==self.__lib.getBook(code).getPublCode()):v=' selected'
            else:v=''
            s+='<option%s value=%s>%s</option>'%(v,str(c),self.__lib.getPubl(c).getName())
        s+='</select>'
        return s

    def authorCombo(self,code=0):
        s='<select name=author>'
        for c in self.__lib.getAuthorCodes():
            if not(c in self.__lib.getBook(code).getAuthorCodes()):
                s+='<option value=%s>%s</option>'%(str(c),self.__lib.getAuthor(c).getBiblioStr())
        s+='</select>'
        return s

    def authorList(self,code=0):
        s='<table>'
        for c in self.__lib.getBook(code).getAuthorCodes():
            s+='''<tr><td>%s</td><td><a href=delauthor?code=%s&acode=%s>удалить</td></tr>
            '''%(self.__lib.getAuthor(c).getBiblioStr(),str(code),str(c))
        s+='</table>'
        return s

    def bookform(self,code=0,add=True):
        name,img,publ,year,pages='','',0,0,0
        if add:a='addaction'
        else: a='editaction?code=%s'%code
        if code in self.__lib.getBookCodes():
            name=self.__lib.getBook(code).getName()
            img=self.__lib.getBook(code).getImg()
            publ=self.__lib.getBook(code).getPublCode()
            year=self.__lib.getBook(code).getYear()
            pages=self.__lib.getBook(code).getPages()
        s='''<form action=%s method=post>
        <table>
        <tr><td>название</td><td><input type=text name=name value='%s'></td></tr>
        <tr><td>обложка</td><td><input type=text name=img value='%s'></td></tr>
        <tr><td>издательство</td><td>%s</td></tr>
        <tr><td>год</td><td><input type=number name=year value=%s></td></tr>
        <tr><td>страницы</td><td><input type=number name=pages value=%s></td></tr>
        <tr><td><input type=submit></td><td></td></tr>
        </table>
        </form>'''%(a,name,img,self.publCombo(publ),str(year),str(pages))
        return s

    def addaction(self,name,img,publ,year,pages):
        self.__lib.newBook(name,img,publ=self.__lib.getPubl(int(publ)),year=int(year),pages=int(pages))
        return 'книга добавлена<br><a href=index>назад</a>'
    addaction.exposed=True

    def addform(self):
        s=u'Добавить новую книгу<br>'
        s+=self.bookform(0)
        return s
    addform.exposed=True

    def editform(self,code):
        s=u'Редактировать книгу<br>'
        s+=self.bookform(int(code),False)
        s+='''авторы
        <form action=addauthor?code=%s method=post>
        <table>
        <tr><td>%s</td><td><input type=submit value=добавить></td>
        </table>
        '''%(str(code),self.authorCombo(int(code)))
        s+=self.authorList(int(code))
        if self.__lib.getBook(int(code)).getImg():
            s="""<table>
            <tr valign=top><td><img src=../static/img/%s></td>
            <td>%s</td></tr>
            </table>
            """%(self.__lib.getBook(int(code)).getImg(),s)
        return s
    editform.exposed=True

    def editaction(self,code,name,img,publ,year,pages):
        self.__lib.getBook(int(code)).setName(name)
        self.__lib.getBook(int(code)).setImg(img)
        self.__lib.getBook(int(code)).setPubl(self.__lib.getPubl(int(publ)))
        self.__lib.getBook(int(code)).setYear(int(year))
        self.__lib.getBook(int(code)).setPages(int(pages))
        return 'книга изменена<br><a href=index>назад</a>'
    editaction.exposed=True

    def addauthor(self,code,author):
        self.__lib.getBook(int(code)).appendAuthor(self.__lib.getAuthor(int(author)))
        return 'автор добавлен<br><a href=editform?code=%s>назад</a>'%str(code)
    addauthor.exposed=True

    def delauthor(self,code,acode):
        self.__lib.getBook(int(code)).removeAuthor(int(acode))
        return 'автор удален<br><a href=editform?code=%s>назад</a>'%str(code)
    delauthor.exposed=True

    def delr(self,code):
        self.__lib.removeBook(int(code))
        return 'книга удалена<br><a href=index>назад</a>'
    delr.exposed=True