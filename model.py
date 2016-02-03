# -*- coding: utf-8 -*-
import web
import sys 
import myconfig
default_encoding = 'utf-8' 
if sys.getdefaultencoding() != default_encoding: 
    reload(sys) 
    sys.setdefaultencoding(default_encoding) 
#     print   "sys encode :%s" % sys.getdefaultencoding() 
# else:
#     print "sys encode utf-8"

db = web.database(dbn='mysql', db='myissuedb', user='root',pw='850201',charset='utf8')

def get_issues():
    try:
        return db.select('issue', where="isArticle=True", order='id desc')
    except:
        print "no this database or table 0."
        # db.query(myconfig.CREATEDB_QUERY)
        db.query(myconfig.CREATETB_QUERY_ISSUE)
        db.query(myconfig.CREATETB_QUERY_USER)

def get_page(n):
    offset = (n-1)*myconfig.NUMBER_IN_PAGE
    return db.select('issue', where="isArticle=True", order='id desc',limit=myconfig.NUMBER_IN_PAGE,offset=offset)

def get_issue(id):
    return db.select('issue',where="id=$id", vars=locals())

def new_issue(title,detail,parent,user,isArticle):
    n = db.insert('issue',title=title,detail=detail,parent=parent,user=user,isArticle=isArticle)
    return n;

def del_issue(id):  
    db.delete('issue', where="id=$id", vars=locals())
    
def get_comments(id):
    return db.select('issue',where="parent=$id",order='id', vars=locals())

def get_users():
    return db.select('user', order='id')

def get_user(id):
    return db.select('user',where="id=$id", vars=locals())

def new_user(name,password):
    n = db.insert('user',name=name,password=password)
    return n

if __name__ == '__main__':
    n = new_issue("hi",u"and hello大饭店梵蒂冈203",1,1,True);
    issues= get_issue(n)
    for  issue in issues:
        print issue.title, issue.detail