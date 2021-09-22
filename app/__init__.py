from flask import Flask

from app import views
from app.configs import database, env_config, migrations


def create_app():
    app = Flask(__name__)

    env_config.init_app(app)
    database.init_app(app)
    migrations.init_app(app)
    views.init_app(app)

    return app
