# 主执行文件
from flask import Flask

from flask_project_structure.factory import create_app, setup_logging
from flask_project_structure import logger
from flask_project_structure.config import get_config

app = application = create_app(get_config())
setup_logging(get_config())

@app.route("/")
def hello():
    return "Hello, Flask!"