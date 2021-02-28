from markdown import markdown
from lxml.etree import HTML


class ArticlMarkdown:

    def __init__(self, article_content):
        self.__article_content = article_content

    def get_brief(self):
        """
        获取简介内容
        """
        html_content = markdown(
            text=self.__article_content, 
            extensions=["markdown.extensions.toc", "markdown.extensions.fenced_code", "markdown.extensions.tables"]
        )
        r = HTML(html_content)
        str_content = r.xpath("string(.)")
        str_content = str_content[:150] if len(str_content) > 100 else str_content
        return str_content + "..."

    def trans_to_html(self):
        html_content = markdown(
            text=self.__article_content, 
            extensions=["markdown.extensions.toc", "markdown.extensions.fenced_code", "markdown.extensions.tables"]
        )
        return html_content
