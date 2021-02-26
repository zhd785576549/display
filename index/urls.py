from index import views
from flask_url.conf import path

urls = [
    path(rule="/", view_func=views.index_view, endpoint="index")
]
