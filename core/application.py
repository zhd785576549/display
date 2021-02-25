import os
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_url.conf import FlaskUrlConf
from flask import Flask

db = SQLAlchemy()


def create_app(import_name):
    """
    创建Flask应用
    :param import_name: [str]  模块名称
    :return:
    """
    f_app = Flask(import_name)
    # 根据环境变量加载配置信息
    env_dict = {
        "DEV": "core.dev_settings",
        "ONLINE": "core.online_settings"
    }
    env = os.environ.get("PRO_ENV", "DEV")
    f_app.config.from_object(env_dict.get(env, "core.dev_settings"))
    Bootstrap(app=f_app)
    FlaskUrlConf(app=f_app)
    db.init_app(app=f_app)
    return f_app


app = create_app(__name__)
