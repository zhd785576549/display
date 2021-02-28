from application import db
from config import models as m_conf
from article import models as m_article


def select_category_list():
    """
    筛选分类信息
    """
    return db.session.query(m_conf.Category).order_by(m_conf.Category.create_time.asc()).all()


def select_article_list_paginate(category_id=None, page=1, page_size=10):
    """
    通过分类查询文章列表

    :param category_id: [int] 分类ID
    :param offset: [int] 偏移量
    :param limit: [int] 限制个数
    """
    query = db.session.query(m_article.Article)
    if category_id:
        query = query.filter(m_article.Article.category_id == category_id)

    return query.paginate(page=page, per_page=page_size)
