from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)

login_manager.init_app(app)

app.config.from_object('app.settings.base')

db = SQLAlchemy()
db.init_app(app)
Migrate(app, db)

bootstrap = Bootstrap(app)

from app.users import models
from app.users import users as users_blueprint

app.register_blueprint(users_blueprint, url_prefix='/users')



