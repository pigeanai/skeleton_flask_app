from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy import select

from app import db
from ..main import bp
from ..models import User


@bp.route("/")
def main():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    return render_template("login.html")


@bp.route("/login", methods = ["POST"])
def login():
    submitted = request.json
    user: User = db.session.scalar(select(User).where(User.username == submitted["uname"]))
    if user is None or not user.check_password(submitted["pword"]):
        return redirect(url_for("main.main"))
    login_user(user)
    return redirect(url_for("main.home"))


@bp.route("/home")
@login_required
def home():
    query = select(User)
    all_users = db.session.scalars(query).all()
    return render_template("home.html", users=all_users)


@bp.route("/add-user", methods = ["POST"])
@login_required
def add_user():
    new_user_params = request.json
    return redirect(url_for("main.home"))


@bp.route('/logout', methods = ["POST"])
def logout():
    logout_user()
    return redirect(url_for("main.main"))