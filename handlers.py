from flask import render_template
from flask.views import MethodView

class Index(MethodView):
    @staticmethod
    def get():
        return render_template("index.html")