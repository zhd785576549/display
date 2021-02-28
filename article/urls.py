from flask_url.conf import path
from article import views


urls = [
    path(rule="/article/page/<int:a_id>/", view_func=views.get_article, endpoint="page")
]
