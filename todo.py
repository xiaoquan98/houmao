""" Basic issue list using webpy 0.3 """
import web
import model
import json

### Url mappings

urls = (
    '/', 'Index',
    '/del/(\d+)', 'Delete',
    '/json/issue/(\d+)','Issue',
    '/json/user/(\d+)','User',
    '/(.*.ico)', 'StaticFile',   
    '/(.*.js)', 'StaticFile', 
   )


### Templates
render = web.template.render('templates', base='base')

class Index:
    def GET(self):
        """ Show page """
        issues = model.get_issues()
        return render.index(issues)

    def POST(self):
        """" do nothing with POST """
        # print "do nothing with POST."
        return

class Delete:
    def POST(self, id):
        """ Delete based on ID """
        id = int(id)
        model.del_issue(id)
        raise web.seeother('/')

class Issue:
    def GET(self, id):
        """ get issue json  """
        id = int(id)
        web.header('Content-Type', 'application/json')
        return json.dumps(list(model.get_issue(id)),sort_keys=True,indent=2)

    def POST(self,id):
        web.header('Content-Type', 'application/json')
        dout = {}
        data = json.loads(web.data().decode("utf-8-sig"));
        try:
            n = model.new_issue(data["title"],data["detail"],"abx","user",data["isArticle"])
            dout["success"] = True
            dout["message"] = list(model.get_issues())
        except (KeyError):
            dout["success"] = False
            dout["errors"] = "Title is required."
        # print json.dumps(dout,sort_keys=True,indent=2)
        return json.dumps(dout,sort_keys=True,indent=2)

class User:
    def GET(self, id):
        """ get user json  """
        id = int(id)
        web.header('Content-Type', 'application/json')
        return json.dumps(list(model.get_user(id)),sort_keys=True,indent=2)

    def POST(self,id):
        n = model.new_user(data["name"],data["password"])
        web.header('Content-Type', 'application/json')
        return json.dumps(list(model.get_user(n)),sort_keys=True,indent=2)

class StaticFile:  
    def GET(self, file):  
        web.seeother('/static/'+file); 

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
