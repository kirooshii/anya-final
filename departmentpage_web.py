class departmentpage:
    def __init__(self,accounting):
        self.__lib=accounting

    def index(self):
        s='''<a href=..>назад</a>/<a href=addform>добавить</a>
        <table border=1 cellpadding=4 cellspacing=0>
        <tr><th bgcolor=gray>#</th>
        <th bgcolor=gray>название</th>
        <th bgcolor=gray>количество сотрудников</th></tr>'''
        r=1
        bg=''
        for c in self.__lib.getDepartmentCodes():
            s+='<tr%s><td>%d</td>'%(bg,r)
            s+='<td>%s</td>'%self.__lib.getDepartment(c).getName()
            s+='<td>%s</td>'%self.__lib.getDepartment(c).getEmployees()
            s+='<td><a href=editform?code=%s>редактировать</a></td>'%c
            s+='<td><a href=delr?code=%s>удалить</a></td></tr>'%c
            r+=1
            if bg:bg=''
            else:bg=' bgcolor=silver'
        s+='</table>'
        return s
    index.exposed=True

    def form(self,code=0,add=True):
        name,employees='',0
        if add:a='addaction'
        else: a='editaction?code=%s'%code
        if code in self.__lib.getDepartmentCodes():
            name=self.__lib.getDepartment(code).getName()
            employees=self.__lib.getDepartment(code).getEmployees()
        s='''<form action=%s method=post>
        <table>
        <tr><td>название</td><td><input type=text name=name value='%s'></td></tr>
        <tr><td>количество сотрудников</td><td><input type=number name=employees value=%s></td></tr>
        <tr><td><input type=submit></td><td></td></tr>
        </table>
        </form>'''%(a,name,str(employees))
        return s

    def addaction(self, name='', employees='', **kwargs):
        self.__lib.newDepartment(name, int(employees) if employees else 0)
        return 'отдел добавлен<br><a href=index>назад</a>'
    addaction.exposed=True

    def addform(self):
        s=u'Добавить новый отдел<br>'
        s+=self.form(0)
        return s
    addform.exposed=True

    def editform(self, code='', **kwargs):
        s=u'Редактировать отдел<br>'
        s+=self.form(int(code) if code else 0, False)
        return s
    editform.exposed=True

    def editaction(self, code='', name='', employees='', **kwargs):
        c = int(code) if code else 0
        if c in self.__lib.getDepartmentCodes():
            self.__lib.getDepartment(c).setName(name)
            self.__lib.getDepartment(c).setEmployees(int(employees) if employees else 0)
        return 'отдел изменен<br><a href=index>назад</a>'
    editaction.exposed=True

    def delr(self, code='', **kwargs):
        if code:
            self.__lib.removeDepartment(int(code))
        return 'отдел удален<br><a href=index>назад</a>'
    delr.exposed=True
