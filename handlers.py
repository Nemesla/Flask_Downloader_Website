from flask import render_template, session, redirect, url_for, request
from flask.views import MethodView

# Page Index class
class Index(MethodView):
    @staticmethod
    def get():
        return render_template("index.html")
    @staticmethod
    def post():
        if request.method == "POST":
            session['username'] = request.form.get("username")
            session['password'] = request.form.get("password")
            return redirect("login.html")
        else:
            return redirect("index.html")

# Succesful auth page
class Login(MethodView):
    staticmethod
    def get():
        return render_template("login.html")


# Page error 404 class
class PageNotFound():
    @staticmethod
    def page_not_found(e):
        return render_template('page404.html'), 404