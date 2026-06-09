import os,xml.dom.minidom
from data import data

class dataxml(data):
    def read(self):
        dom=xml.dom.minidom.parse(self.getInp())
        dom.normalize()
        for node in dom.childNodes[0].childNodes:
            if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=='author'):
                code,surname,name,secname=0,"","",""
                for t in node.attributes.items():
                    if t[0]=="code":code=int(t[1])
                    if t[0]=="name":name=t[1]
                    if t[0]=="surname":surname=t[1]
                    if t[0]=="secname":secname=t[1]
                self.getLib().createAuthor(code,surname,name,secname)
            if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=='publ'):
                code,name,shortname=0,"",""
                for t in node.attributes.items():
                    if t[0]=="code":code=int(t[1])
                    if t[0]=="name":name=t[1]
                    if t[0]=="shortname":shortname=t[1]
                self.getLib().createPubl(code,name,shortname)
            if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=='book'):
                code,name,img,publ,year,pages=0,'','',None,0,0
                for t in node.attributes.items():
                    if t[0]=="code":code=int(t[1])
                    if t[0]=="name":name=t[1]
                    if t[0]=="img":img=t[1]
                    if t[0]=="year":year=int(t[1])
                    if t[0]=="pages":pages=int(t[1])
                    if t[0]=="publ":publ=self.getLib().getPubl(int(t[1]))
                book=self.getLib().createBook(code,name,img,publ,year,pages)
                for n in node.childNodes:
                    if (n.nodeType==n.ELEMENT_NODE)and(n.nodeName=='author'):
                        for t in n.attributes.items():
                            if t[0]=="code":author=self.getLib().getAuthor(int(t[1]))
                        book.appendAuthor(author)
    def write(self):
        dom=xml.dom.minidom.Document()
        root=dom.createElement("library")
        dom.appendChild(root)
        for a in self.getLib().getAuthorList():
            aut=dom.createElement("author")
            aut.setAttribute('code',str(a.getCode()))
            aut.setAttribute('surname',a.getSurname())
            aut.setAttribute('name',a.getName())
            aut.setAttribute('secname',a.getSecname())
            root.appendChild(aut)
        for p in self.getLib().getPublList():
            pub=dom.createElement("publ")
            pub.setAttribute('code',str(p.getCode()))
            pub.setAttribute('name',p.getName())
            pub.setAttribute('shortname',p.getShortname())
            root.appendChild(pub)
        for b in self.getLib().getBookList():
            bk=dom.createElement("book")
            bk.setAttribute('code',str(b.getCode()))
            bk.setAttribute('name',b.getName())
            bk.setAttribute('img',b.getImg())
            bk.setAttribute('year',str(b.getYear()))
            bk.setAttribute('pages',str(b.getPages()))
            bk.setAttribute('publ',str(b.getPublCode()))
            for ac in b.getAuthorCodes():
                aut=dom.createElement("author")
                aut.setAttribute('code',str(ac))
                bk.appendChild(aut)
            root.appendChild(bk)
        f = open(self.getOut(),"w",encoding='utf-8')
        f.write(dom.toprettyxml())