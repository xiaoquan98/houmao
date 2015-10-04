""" Basic issue list using webpy 0.3 """
import web
import model
import json

### Url mappings

urls = (
    '/', 'Index',
    '/v1/issues','Issues',
    '/v1/issues/(\d+)','Issue',
    '/v1/users/(\d+)','User',
    '/(.*.ico)', 'StaticFile',   
    '/(.*.js)', 'StaticFile', 
    '/(.*.css)', 'StaticFile', 
   )


### Templates
render = web.template.render('templates', base='base')

class Index:
    def GET(self):
        """ Show page """
        issues = list(model.get_issues())
        return render.index(json.dumps(issues))

    def POST(self):
        """" do nothing with POST """
        # print "do nothing with POST."
        return


class Issues:
    def GET(self):
        """ get issue json  """
        web.header('Content-Type', 'application/json')
        dout = {};
        dout["success"] = True
        dout["message"] = list(model.get_issues())
        return json.dumps(dout,sort_keys=True,indent=2)
        
class Issue:
    def GET(self, id):
        """ get issue json  """
        id = int(id)
        web.header('Content-Type', 'application/json')
        dout = {};
        dout["success"] = True
        dout["message"] = list(model.get_issue(id))
        return json.dumps(dout,sort_keys=True,indent=2)

    def POST(self,id):
        web.header('Content-Type', 'application/json')
        dout = {}
        din = json.loads(web.data().decode("utf-8-sig"));
        try:
            n = model.new_issue(din["title"],din["detail"],"abx","user",din["isArticle"])
            dout["success"] = True
            dout["message"] = list(model.get_issues())
        except (KeyError):
            dout["success"] = False
            dout["errors"] = "Title is required."
        finally:
            # print json.dumps(dout,sort_keys=True,indent=2)
            return json.dumps(dout,sort_keys=True,indent=2)
            
    def DELETE(self,id):
        web.header('Content-Type', 'application/json')
        id = int(id)
        dout = {}
        model.del_issue(id)
        # dout["success"] = True
        # return json.dumps(dout,sort_keys=True,indent=2)
        dout = {};
        dout["success"] = True
        dout["message"] = list(model.get_issues())
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
