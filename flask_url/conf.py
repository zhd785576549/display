from flask import Flask
from flask.blueprints import Blueprint
from flask_url.utils import get_mod_attr


def path(rule, endpoint, view_func, **options):
    return Url(rule=rule, endpoint=endpoint, view_func=view_func, **options)


class Url:
    rule = None
    endpoint = None
    view_func = None
    options = {}

    def __init__(self, rule, endpoint, view_func, **options):
        self.rule = rule
        self.endpoint = endpoint
        self.view_func = view_func
        self.options = options


class FlaskUrlConf:

    def __init__(self, app: Flask = None):
        if app:
            self.init_app(app=app)

    def init_app(self, app: Flask):
        install_apps = app.config.get("INSTALL_APPS", [])
        for app_str in install_apps:
            mod_path = f"{app_str}.urls"
            try:
                urls = get_mod_attr(mod_path, "urls")
                b = Blueprint(import_name=mod_path, name=app_str)
                for url in urls:
                    if isinstance(url, Url):
                        b.add_url_rule(
                            rule=url.rule,
                            endpoint=url.endpoint,
                            view_func=url.view_func,
                            **url.options
                        )
                app.register_blueprint(b)
            except ImportError as e:
                app.logger.warn(f"Import module {mod_path} err {e}")
            except IndexError as e:
                app.logger.warn(f"Split module {mod_path} attr error {e}")
            except AttributeError as e:
                app.logger.warn(f"Get attr from url module {mod_path}, error {e}")
