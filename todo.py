""" Basic issue list using webpy 0.3 """
import web
import model
import json
import datetime
import myconfig

web.config.debug = False

### Url mappings

urls = (
    '/', 'Index',
    '/v2/issues/issue-(\d+)','Issue',
    '/v2/issues/page-(\d+)','Page',
    '/v2/issues/issue-(\d+)/children','Children',
    '/v2/issues/issue-(\d+)/ancestors','Ancestors',
    '/v1/issues','Issues',
    '/v1/issues/(\d+)','Issue',
    '/v1/users/(\d+)','User',
    '/(.*.ico)', 'StaticFile',   
    '/(.*.js)', 'StaticFile', 
    '/(.*.css)', 'StaticFile', 
    '/view/(.*.html)','StaticFile',
    '/logup','Logup',
    '/login','Login',
    '/logout','Logout',
   )


### Templates
render = web.template.render('templates', base='base')

json_serial = lambda obj: (
    obj.isoformat()
    if isinstance(obj, datetime.datetime)
    or isinstance(obj, datetime.date)
    else None
)

def Auth(func):
    def wrapper(*args, **kwargs):
        sessionhook()
        au = session.get('access_token', "false")
        if au == 'true':
            return func(*args, **kwargs)
        return "not auth."
    return wrapper
    
class Index:
    def GET(self):
        """ Show page """
        return render.index()

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
        print json.dumps(dout,sort_keys=True,indent=2,default=json_serial)
        return json.dumps(dout,sort_keys=True,indent=2,default=json_serial)
        
class Page:
    def GET(self, n):
        """ get issue json  """
        n = int(n)
        web.header('Content-Type', 'application/json')
        dout = {};
        dout["success"] = True
        dout["message"] = list(model.get_page(n))
        return json.dumps(dout,sort_keys=True,indent=2,default=json_serial)
        
class Children:
    def GET(self, n):
        """ get issue json  """
        n = int(n)
        web.header('Content-Type', 'application/json')
        dout = {};
        dout["success"] = True
        dout["message"] = list(model.get_comments(n))
        print json.dumps(dout,sort_keys=True,indent=2,default=json_serial)
        return json.dumps(dout,sort_keys=True,indent=2,default=json_serial)
        
class Issue:
    def GET(self, id):
        """ get issue json  """
        id = int(id)
        web.header('Content-Type', 'application/json')
        dout = {};
        dout["success"] = True
        dout["message"] = list(model.get_issue(id))
        return json.dumps(dout,sort_keys=True,indent=2,default=json_serial)

    @Auth
    def POST(self,id):
        web.header('Content-Type', 'application/json')
        dout = {}
        din = json.loads(web.data().decode("utf-8-sig"));
        
        print "din: " + json.dumps(din,sort_keys=True,indent=2)
        if not din["parent"]:
            din["parent"] = 0;# root mao
        try:
            if not "title" in din:
                # print "add title."
                din["title"] = "";
            n = model.new_issue(din["title"],din["detail"],din["parent"],din["user"],din["isArticle"])
            dout["success"] = True
            dout["message"] = list(model.get_issues())
        except KeyError:
            dout["success"] = False
            dout["errors"] = "Title is required."
        finally:
            # print json.dumps(dout,sort_keys=True,indent=2)
            return json.dumps(dout,sort_keys=True,indent=2,default=json_serial)
            
    @Auth
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
        return json.dumps(dout,sort_keys=True,indent=2,default=json_serial)


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
    
# session & user login 
def sessionhook():
    global session
    # Hack to make session play nice with the reloader (in debug mode)
    if web.config.get('_session') is None:
        db = model.db
        store = web.session.DBStore(db, 'sessions')
        session = web.session.Session(app, store, initializer={'access_token': "false"})
        web.config._session = session
    else:
        session = web.config._session
        
        
class Logup:
    def POST(self):
        sessionhook()
        
        web.header('Content-Type', 'application/json')
        dout = {}
        
        i = json.loads(web.data().decode("utf-8-sig"));
        username =i.get('name',None)
        password =i.get('password',None)
        
        session = web.config._session
        if model.new_user(username,password): 
        # if username == 'abcd' and password == '1234':
            session.access_token = 'true'
            # print "check user ok."
            dout["success"] = True
        else:
            session.access_token = 'false'
            dout["success"] = False
        return json.dumps(dout,sort_keys=True,indent=2,default=json_serial)
        
class Login:
    def POST(self):
        sessionhook()
        
        web.header('Content-Type', 'application/json')
        dout = {}
        
        i = json.loads(web.data().decode("utf-8-sig"));
        username =i.get('name',None)
        password =i.get('password',None)
        
        session = web.config._session
        if model.check_user(username,password): 
        # if username == 'abcd' and password == '1234':
            session.access_token = 'true'
            # print "check user ok."
            dout["success"] = True
        else:
            session.access_token = 'false'
            dout["success"] = False
        return json.dumps(dout,sort_keys=True,indent=2,default=json_serial)

class Logout:
    def POST(self):
        sessionhook()
        
        web.header('Content-Type', 'application/json')
        dout = {}
        session = web.config._session
        session.access_token = 'false'
        # print "check user ok."
        dout["success"] = True
        return json.dumps(dout,sort_keys=True,indent=2,default=json_serial)
        
app = web.application(urls, globals())


if __name__ == '__main__':
    app.run()
