from app import create_app
from app.controllers.users import add_initial_user_if_required

app = create_app()
add_initial_user_if_required(app)