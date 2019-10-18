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
    mongo.init_app(app)
    mysql.init_app(app)
    redis.init_app(app)

def create_app(config: dict) -> Flask:
    app = Flask("flask_project_structure", static_folder=None)
    app.config.from_mapping(config)
    level = app.config.get("LOG_LEVEL", "INFO").upper()
    logger.setLevel(level=getattr(logging, level))
    logger.debug("system init")

    _register_blueprint(app)
    _register_extension(app)

    return app

def setup_logging(config) -> None:
    basic_level = config.get("LOG_LEVEL", "INFO").upper()
    logger.setLevel(level=basic_level)

    formatter = logging.Formatter(
        "[%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s/%(process)s] %(message)s"
    )
    if logger.hasHandlers():
        for h in logger.handlers:  # type: logging.Handler
            h.setFormatter(formatter)
    else:
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)