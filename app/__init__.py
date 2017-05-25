from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.config.from_object('app.settings.base')

db = SQLAlchemy()
db.init_app(app)
bootstrap = Bootstrap(app)
Migrate(app, db)

from . import users




