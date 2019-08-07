# flask初始化配置
import logging

from flask import Flask
from flask_project_structure import logger
from flask_project_structure.utils.flask_ext import (
    Mongo, Redis, Mysql
)

mongo = Mongo(appname="flask_project_structure")
redis = Redis()
mysql = Mysql(appname="flask_project_structure")

def _register_blueprint(app: Flask) -> None:
    # from flask_project_structure.views.xxxx import bp
    # app.register_blueprint(bp)
    pass

def _register_extension(app: Flask) -> None:
    mongo.init_app(app, connect=False)
    mysql.init_app(app)
    redis.init_app(app)

def create_app(config: dict) -> Flask:
    app = Flask("rqams", static_folder=None)
    app.config.from_mapping(config)
    level = app.config.get("LOG_LEVEL", "INFO").upper()
    logger.setLevel(level=getattr(logging, level))
    logger.debug("system init")

    _register_blueprint(app)
    _register_extension(app)

    health_check_url = config.get("HEALTH_CHECK_URL")
    if health_check_url:
        _register_health_check(app, health_check_url)

    return app