from handlers import Index

class Routes():
    @staticmethod
    def set(app):
        app.add_url_rule("/", view_func=Index.as_view('/'))
        return app