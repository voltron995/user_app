from . import app
from .users.urls import users

app.register_blueprint(users, url_prefix='/users')