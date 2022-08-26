from flask import Flask

from app.views.fight import fight_bp
from app.views.start import start_bp


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    app.register_blueprint(fight_bp)
    app.register_blueprint(start_bp)

    return app