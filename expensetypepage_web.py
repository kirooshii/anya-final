class expensetypepage:
    def __init__(self,accounting):
        self.__lib=accounting

    def index(self):
        s='''<a href=..>назад</a>/<a href=addform>добавить</a>
        <table border=1 cellpadding=4 cellspacing=0>
        <tr><th bgcolor=gray>#</th>
        <th bgcolor=gray>название</th>
        <th bgcolor=gray>описание</th>
        <th bgcolor=gray>предельная норма</th></tr>'''
        r=1
        bg=''
        for c in self.__lib.getExpenseTypeCodes():
            s+='<tr%s><td>%d</td>'%(bg,r)
            s+='<td>%s</td>'%self.__lib.getExpenseType(c).getName()
            s+='<td>%s</td>'%self.__lib.getExpenseType(c).getDescription()
            s+='<td>%s</td>'%self.__lib.getExpenseType(c).getLimit()
            s+='<td><a href=editform?code=%s>редактировать</a></td>'%c
            s+='<td><a href=delr?code=%s>удалить</a></td></tr>'%c
            r+=1
            if bg:bg=''
            else:bg=' bgcolor=silver'
        s+='</table>'
        return s
    index.exposed=True

    def form(self,code=0,add=True):
        name,description,limit='','',0
        if add:a='addaction'
        else: a='editaction?code=%s'%code
        if code in self.__lib.getExpenseTypeCodes():
            name=self.__lib.getExpenseType(code).getName()
            description=self.__lib.getExpenseType(code).getDescription()
            limit=self.__lib.getExpenseType(code).getLimit()
        s='''<form action=%s method=post>
        <table>
        <tr><td>название</td><td><input type=text name=name value='%s'></td></tr>
        <tr><td>описание</td><td><input type=text name=description value='%s'></td></tr>
        <tr><td>предельная норма</td><td><input type=number step=any name=limit value=%s></td></tr>
        <tr><td><input type=submit></td><td></td></tr>
        </table>
        </form>'''%(a,name,description,str(limit))
        return s

    def addaction(self, name='', description='', limit='', **kwargs):
        self.__lib.newExpenseType(name, description, float(limit) if limit else 0)
        return 'вид расхода добавлен<br><a href=index>назад</a>'
    addaction.exposed=True

    def addform(self):
        s=u'Добавить новый вид расхода<br>'
        s+=self.form(0)
        return s
    addform.exposed=True

    def editform(self, code='', **kwargs):
        s=u'Редактировать вид расхода<br>'
        s+=self.form(int(code) if code else 0, False)
        return s
    editform.exposed=True

    def editaction(self, code='', name='', description='', limit='', **kwargs):
        c = int(code) if code else 0
        if c in self.__lib.getExpenseTypeCodes():
            self.__lib.getExpenseType(c).setName(name)
            self.__lib.getExpenseType(c).setDescription(description)
            self.__lib.getExpenseType(c).setLimit(float(limit) if limit else 0)
        return 'вид расхода изменен<br><a href=index>назад</a>'
    editaction.exposed=True

    def delr(self, code='', **kwargs):
        if code:
            self.__lib.removeExpenseType(int(code))
        return 'вид расхода удален<br><a href=index>назад</a>'
    delr.exposed=True
