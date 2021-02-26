from flask import render_template


def index_view():
    """
    主页面
    :return:
    """
    return render_template("index.html")
