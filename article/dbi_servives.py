from article import dbis as d_article


def get_article_info(article_id):
    """
    获取文章信息

    :param article_id: [int] 文章ID
    """
    return d_article.select_article_by_id(article_id=article_id)
