from ..main import bp
from flask import render_template, current_app
from .. import db

from ..controllers.example_table_controller import get_all_example_table_entries

@bp.route('/')
def main():
    with current_app.app_context():
        all_entries = get_all_example_table_entries(db.session)
    return render_template('index.html', entries = all_entries)