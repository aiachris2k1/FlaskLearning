# coding=utf-8
class Config(object):
    pass


class DevConfig(object):
    debug = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/flasky_learning"


class ProdConfing(object):
    pass
