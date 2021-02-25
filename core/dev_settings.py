from sqlalchemy import pool


DEBUG = True

SECRET_KEY = b'\x17\x82\x15F\xadH\x93\xa9\xff$\x90\xd0\x0c\x06"IS-\xd4\xd74\xdd\x91\xa1:6\xb7+k\x82\x99\x1e'

INSTALL_APPS = [
    "index",
    "article"
]

SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ENGINE_OPTIONS = {
    "pool_pre_ping": True,
    "convert_unicode": True,
    "poolclass": pool.QueuePool,
    "pool_size": 200,
    "pool_recycle": 3600
}

SQLALCHEMY_BINDS = {
    # 展示平台
    "default": "mysql://root:zhd19871111@localhost:3306/exhibition?charset=utf8mb4",
}

