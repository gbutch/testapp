import web

urls = (
    '/', 'index'
)

app = web.application(urls,globals())
render = web.template.render('templates/')

class Index(object):
    def GET(self):
        return render.index()

if __name__ == "__main__":
    app.run()