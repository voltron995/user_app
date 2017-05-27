from flask_migrate import MigrateCommand
from flask_script import Manager
from werkzeug.contrib.fixers import ProxyFix

from app import app

app.wsgi_app = ProxyFix(app.wsgi_app)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
