from core.application import db
from sqlalchemy import Column, Integer, DateTime, String
from datetime import datetime


class Category(db.Model):
    __tablename__ = "category"
    __bind_key__ = "default"

    id = Column(Integer, primary_key=True, autoincrement=True, info="主键")
    name = Column(String(50), nullable=False, default="", info="分类名称")
    parent_id = Column(Integer, nullable=True, default=None, info="父级分类ID")
    create_time = Column(DateTime, nullable=True, default=datetime.now, info="创建时间")
    update_time = Column(DateTime, nullable=True, default=datetime.now, onupdate=datetime.now, info="更新时间")
