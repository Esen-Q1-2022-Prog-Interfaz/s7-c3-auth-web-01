from flask import Blueprint, render_template
from forms.registerForm import RegisterForm
from forms.loginForm import LoginForm

auth = Blueprint("auth", __name__)


@auth.route("/")
def home():
    return render_template("home.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", form=form)


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    return render_template("register.html", form=form)


@auth.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
