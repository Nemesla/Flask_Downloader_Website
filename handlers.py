from flask import render_template
from flask.views import MethodView

# Page Index class
class Index(MethodView):
    @staticmethod
    def get():
        return render_template("index.html")
    
# Page error 404 class
class PageNotFound():
    @staticmethod
    def page_not_found(e):
        return render_template('page404.html'), 404