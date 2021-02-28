from article import models as m_article
from application import db


def select_article_by_id(article_id):
    """
    根据文章ID查找文章信息

    :param article_id: [int] 文章ID
    """
    article = db.session.query(m_article.Article).filter(m_article.Article.id == article_id).first()
    return article
