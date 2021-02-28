from flask import render_template
from flask import request
from index import dbi_services as d_s_index
from utils import md


def index_view():
    """
    主页面
    :return:
    """
    category_id = request.args.get("c_id", None)
    page = request.args.get("page", 1)
    page_size = request.args.get("page_size", 20)
    article_list = d_s_index.get_article_list(category_id=category_id, page=page, page_size=page_size)
    for article in article_list.items:
        article.brief = article.brief or md.ArticlMarkdown(article.content).get_brief()
    context = {
        "category_list": d_s_index.get_category_list(),
        "pagination": article_list
    }
    return render_template("index.html", **context)
