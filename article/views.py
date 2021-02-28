from flask import render_template
from article import dbi_servives as d_s_article

def get_article(a_id):
    article = d_s_article.get_article_info(article_id=a_id)
    context = {
        "article": article
    }
    return render_template("article.html", **context)
    