""" Basic todo list using webpy 0.3 """
import web
import model

### Url mappings

urls = (
    '/', 'Index',
    '/del/(\d+)', 'Delete'
       )


### Templates
render = web.template.render('templates', base='base')


class Index:

    form = web.form.Form(
        web.form.Textbox('title', web.form.notnull, description="I need to:"),
        web.form.Textbox('detail',web.form.notnull,description="description"),
        web.form.Checkbox('isArticle'),
        web.form.Button('Add todo'),
    )

    def GET(self):
        """ Show page """
        todos = model.get_issues()
        form = self.form()
        return render.index(todos, form)

    def POST(self):
        """ Add new entry """
        form = self.form()
        if not form.validates():
            # todos = model.get_todos()
            todos = model.get_issues()
            return render.index(todos, form)
        # model.new_todo(form.d.title)
        model.new_issue(form.d.title,form.d.detail,"abx","user",form.d.isArticle)
        raise web.seeother('/')


class Delete:

    def POST(self, id):
        """ Delete based on ID """
        id = int(id)
        model.del_todo(id)
        raise web.seeother('/')


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
