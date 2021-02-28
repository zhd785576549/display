from flask import render_template
from flask import abort
from article import dbi_servives as d_s_article
from utils import md

def get_article(a_id):
    article = d_s_article.get_article_info(article_id=a_id)
    if article is None:
        abort(404)
    article.content = md.ArticlMarkdown(article.content).trans_to_html()
    context = {
        "article": article
    }
    return render_template("article.html", **context)
    