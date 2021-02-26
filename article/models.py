from application import db
from sqlalchemy import Column, Integer, DateTime, String, Text
from datetime import datetime


class Article(db.Model):
    __tablename__ = "category"
    __bind_key__ = "default"

    id = Column(Integer, primary_key=True, autoincrement=True, info="主键")
    title = Column(String(200), nullable=False, info="标题")
    content = Column(Text, nullable=True, info="内容")
    category_id = Column(Integer, nullable=False, info="分类ID")
    create_time = Column(DateTime, nullable=True, default=datetime.now, info="创建时间")
    update_time = Column(DateTime, nullable=True, default=datetime.now, onupdate=datetime.now, info="更新时间")
