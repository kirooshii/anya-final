import os,xml.dom.minidom
from data import data

class dataxml(data):
    def read(self):
        dom=xml.dom.minidom.parse(self.getInp())
        dom.normalize()
        for node in dom.childNodes[0].childNodes:
            if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=='department'):
                code,name,employees=0,"",0
                for t in node.attributes.items():
                    if t[0]=="code":code=int(t[1])
                    if t[0]=="name":name=t[1]
                    if t[0]=="employees":employees=int(t[1])
                self.getLib().createDepartment(code,name,employees)
            if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=='expensetype'):
                code,name,description,limit=0,"","",0
                for t in node.attributes.items():
                    if t[0]=="code":code=int(t[1])
                    if t[0]=="name":name=t[1]
                    if t[0]=="description":description=t[1]
                    if t[0]=="limit":limit=float(t[1])
                self.getLib().createExpenseType(code,name,description,limit)
            if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=='expense'):
                code,name,expensetype,department,amount,date=0,'',None,None,0,''
                for t in node.attributes.items():
                    if t[0]=="code":code=int(t[1])
                    if t[0]=="name":name=t[1]
                    if t[0]=="amount":amount=float(t[1])
                    if t[0]=="date":date=t[1]
                    if t[0]=="expensetype":expensetype=self.getLib().getExpenseType(int(t[1]))
                    if t[0]=="department":department=self.getLib().getDepartment(int(t[1]))
                self.getLib().createExpense(code,name,expensetype,department,amount,date)
    def write(self):
        dom=xml.dom.minidom.Document()
        root=dom.createElement("accounting")
        dom.appendChild(root)
        for d in self.getLib().getDepartmentList():
            dep=dom.createElement("department")
            dep.setAttribute('code',str(d.getCode()))
            dep.setAttribute('name',d.getName())
            dep.setAttribute('employees',str(d.getEmployees()))
            root.appendChild(dep)
        for t in self.getLib().getExpenseTypeList():
            et=dom.createElement("expensetype")
            et.setAttribute('code',str(t.getCode()))
            et.setAttribute('name',t.getName())
            et.setAttribute('description',t.getDescription())
            et.setAttribute('limit',str(t.getLimit()))
            root.appendChild(et)
        for e in self.getLib().getExpenseList():
            exp=dom.createElement("expense")
            exp.setAttribute('code',str(e.getCode()))
            exp.setAttribute('name',e.getName())
            exp.setAttribute('amount',str(e.getAmount()))
            exp.setAttribute('date',e.getDate())
            exp.setAttribute('expensetype',str(e.getExpenseTypeCode()))
            exp.setAttribute('department',str(e.getDepartmentCode()))
            root.appendChild(exp)
        f = open(self.getOut(),"w",encoding='utf-8')
        f.write(dom.toprettyxml())
