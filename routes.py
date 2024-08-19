from handlers import Index, PageNotFound, Login


class Routes():
    @staticmethod
    def set(app):
        app.add_url_rule("/", view_func=Index.as_view('/'), methods=["GET", "POST"])
        app.add_url_rule("/index", view_func=Index.as_view("index"), methods=["GET", "POST"])
        app.add_url_rule("/login", view_func=Login.as_view("login"), methods=["GET"])
        app.register_error_handler(404, PageNotFound.page_not_found)
        return app