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

    form = web.form.Form(
        web.form.Textbox('title', web.form.notnull, description="I need to:"),
        web.form.Textbox('detail',web.form.notnull,description="description"),
        web.form.Checkbox('isArticle'),
        web.form.Button('Add issue'),
    )

    def GET(self):
        """ Show page """
        issues = model.get_issues()
        form = self.form()
        return render.index(issues, form)

    def POST(self):
        """ Add new entry """
        form = self.form()
        if not form.validates():
            # issues = model.get_issues()
            issues = model.get_issues()
            return render.index(issues, form)
        # model.new_issue(form.d.title)
        model.new_issue(form.d.title,form.d.detail,"abx","user",form.d.isArticle)
        raise web.seeother('/')


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
        # print json.dumps(list(model.get_issue(id)),sort_keys=True,indent=2)
        return json.dumps(list(model.get_issue(id)),sort_keys=True,indent=2)

class User:

    def GET(self, id):
        """ get user json  """
        id = int(id)
        web.header('Content-Type', 'application/json')
        return json.dumps(list(model.get_user(id)),sort_keys=True,indent=2)

class StaticFile:  
    def GET(self, file):  
        web.seeother('/static/'+file); 

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
