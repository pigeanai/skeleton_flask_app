from app.main import bp
from flask import render_template

@bp.route('/')
def main():
    return render_template('index.html')