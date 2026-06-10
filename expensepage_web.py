class expensepage:
    def __init__(self,accounting):
        self.__lib=accounting

    def index(self):
        s='''<a href=..>назад</a>/<a href=addform>добавить</a>
        <table border=1 cellpadding=4 cellspacing=0>
        <tr><th bgcolor=gray>#</th>
        <th bgcolor=gray>вид расхода</th>
        <th bgcolor=gray>отдел</th>
        <th bgcolor=gray>сумма</th>
        <th bgcolor=gray>дата</th></tr>'''
        r=1
        bg=''
        for c in self.__lib.getExpenseCodes():
            s+='<tr%s><td>%d</td>'%(bg,r)
            s+='<td>%s</td>'%self.__lib.getExpense(c).getExpenseTypeName()
            s+='<td>%s</td>'%self.__lib.getExpense(c).getDepartmentName()
            s+='<td>%s</td>'%self.__lib.getExpense(c).getAmount()
            s+='<td>%s</td>'%self.__lib.getExpense(c).getDate()
            s+='<td><a href=editform?code=%s>редактировать</a></td>'%c
            s+='<td><a href=delr?code=%s>удалить</a></td></tr>'%c
            r+=1
            if bg:bg=''
            else:bg=' bgcolor=silver'
        s+='</table>'
        return s
    index.exposed=True

    def expensetypeCombo(self,code=0):
        s='<select name=expensetype>'
        for c in self.__lib.getExpenseTypeCodes():
            if (code in self.__lib.getExpenseCodes())and(c==self.__lib.getExpense(code).getExpenseTypeCode()):v=' selected'
            else:v=''
            s+='<option%s value=%s>%s</option>'%(v,str(c),self.__lib.getExpenseType(c).getName())
        s+='</select>'
        return s

    def departmentCombo(self,code=0):
        s='<select name=department>'
        for c in self.__lib.getDepartmentCodes():
            if (code in self.__lib.getExpenseCodes())and(c==self.__lib.getExpense(code).getDepartmentCode()):v=' selected'
            else:v=''
            s+='<option%s value=%s>%s</option>'%(v,str(c),self.__lib.getDepartment(c).getName())
        s+='</select>'
        return s

    def form(self,code=0,add=True):
        expensetype,department,amount,date=0,0,0,''
        if add:a='addaction'
        else: a='editaction?code=%s'%code
        if code in self.__lib.getExpenseCodes():
            expensetype=self.__lib.getExpense(code).getExpenseTypeCode()
            department=self.__lib.getExpense(code).getDepartmentCode()
            amount=self.__lib.getExpense(code).getAmount()
            date=self.__lib.getExpense(code).getDate()
        s='''<form action=%s method=post>
        <table>
        <tr><td>вид расхода</td><td>%s</td></tr>
        <tr><td>отдел</td><td>%s</td></tr>
        <tr><td>сумма</td><td><input type=number step=any name=amount value=%s></td></tr>
        <tr><td>дата</td><td><input type=text name=date value='%s'></td></tr>
        <tr><td><input type=submit></td><td></td></tr>
        </table>
        </form>'''%(a,self.expensetypeCombo(expensetype),self.departmentCombo(department),str(amount),date)
        return s

    def addaction(self, expensetype='', department='', amount='', date='', **kwargs):
        if expensetype and department:
            self.__lib.newExpense('',
                self.__lib.getExpenseType(int(expensetype)),
                self.__lib.getDepartment(int(department)),
                float(amount) if amount else 0, date)
        return 'расход добавлен<br><a href=index>назад</a>'
    addaction.exposed=True

    def addform(self):
        s=u'Добавить новый расход<br>'
        s+=self.form(0)
        return s
    addform.exposed=True

    def editform(self, code='', **kwargs):
        s=u'Редактировать расход<br>'
        s+=self.form(int(code) if code else 0, False)
        return s
    editform.exposed=True

    def editaction(self, code='', expensetype='', department='', amount='', date='', **kwargs):
        c = int(code) if code else 0
        if c in self.__lib.getExpenseCodes():
            if expensetype:
                self.__lib.getExpense(c).setExpenseType(self.__lib.getExpenseType(int(expensetype)))
            if department:
                self.__lib.getExpense(c).setDepartment(self.__lib.getDepartment(int(department)))
            self.__lib.getExpense(c).setAmount(float(amount) if amount else 0)
            self.__lib.getExpense(c).setDate(date)
        return 'расход изменен<br><a href=index>назад</a>'
    editaction.exposed=True

    def delr(self, code='', **kwargs):
        if code:
            self.__lib.removeExpense(int(code))
        return 'расход удален<br><a href=index>назад</a>'
    delr.exposed=True
