from flask import Flask
from sqlalchemy import select

from app import db
from config import Config
from ..models import User

def add_initial_user_if_required(app: Flask):
    with app.app_context():
        query = select(User)
        all_users = db.session.scalars(query).all()
        if len(all_users) >= 1:
            
            return
        if not Config.DEFAULT_USER or not Config.DEFAULT_USER_PASS:
            app.logger.error("A DEFAULT_USER and DEFAULT_USER_PASS must be set as environment variables")
            exit(1)
        user = User(username=Config.DEFAULT_USER)
        user.set_password(Config.DEFAULT_USER_PASS)
        db.session.add(user)
        db.session.commit()
        app.logger.info(f"Default user '{Config.DEFAULT_USER}' has been added")