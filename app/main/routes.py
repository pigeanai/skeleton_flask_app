from flask import render_template, redirect, url_for, request, abort
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
    user: User = db.session.scalar(select(User).where(User.username == submitted["username"]))
    if user is None or not user.check_password(submitted["password"]):
        return redirect(url_for("main.main"))
    login_user(user, remember=True)
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
    if new_user_params["password"] != new_user_params["password-confirm"]:
        return {"error": "Passwords do not match"}, 400
    new_user = User(username=new_user_params["uname"], email=new_user_params["email"])
    new_user.set_password(new_user_params["password"])
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("main.home"))


@bp.route("/delete-user/<user_id>", methods = ["POST"])
@login_required
def delete_user(user_id: int):
    query = select(User).filter_by(id=user_id)
    # https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.MappingResult
    user = db.session.scalar(query)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("main.home"))


@bp.route('/logout', methods = ["POST"])
def logout():
    logout_user()
    return redirect(url_for("main.main"))