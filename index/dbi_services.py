from index import dbis as d_index


def get_category_list():
    """
    获取分类列表数据
    """
    category_list = d_index.select_category_list()
    return category_list


def get_article_list(category_id=None, page=1, page_size=10):
    """
    获取文章列表

    :param category_id: [int] 分类ID
    :param offset: [int] 偏移量
    :param limit: [int] 限制个数
    """
    return d_index.select_article_list_paginate(category_id=category_id, page=page, page_size=page_size)
