from handlers import Index, PageNotFound


class Routes():
    @staticmethod
    def set(app):
        app.add_url_rule("/", view_func=Index.as_view('/'))
        app.register_error_handler(404, PageNotFound.page_not_found)
        return app