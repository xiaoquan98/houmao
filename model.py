import web

db = web.database(dbn='mysql', db='issuedb', user='root',pw='idore')

def get_issues():
	return db.select('issue', order='id')

def new_issue(text):
	db.insert('issue', title=text)

def del_issue(id):  
	db.delete('issue', where="id=$id", vars=locals())

def new_issue(title,detail,parent,user,isArticle):
 	db.insert('issue',title=title,detail=detail,parent=parent,user=user,isArticle=isArticle)

def get_issues():
	return db.select('issue',order='id')

def  get_issue(id):
	return db.select('issue',where="id=$id", vars=locals())

def  get_user(id):
	return db.select('user',where="id=$id", vars=locals())

if __name__ == '__main__':
	get_issue(1)