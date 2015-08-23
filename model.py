import web

db = web.database(dbn='mysql', db='demodb', user='dbidore',pw='idore')

def get_todos():
	return db.select('todo', order='id')

def new_todo(text):
	db.insert('todo', title=text)

def del_todo(id):  
	db.delete('todo', where="id=$id", vars=locals())

def new_issue(title,detail,parent,user,isArticle):
 	db.insert('todo',title=title,detail=detail,parent=parent,user=user,isArticle=isArticle)

def get_issues():
	return db.select('todo',order='id')

def  get_issue(id):
	return db.select('todo',where="id=$id", vars=locals())

def  get_user(id):
	return db.select('user',where="id=$id", vars=locals())

if __name__ == '__main__':
	get_issue(1)