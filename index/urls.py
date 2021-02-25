from flask.blueprints import Blueprint
from index import views

urls = Blueprint("index", __name__)

urls.add_url_rule()
