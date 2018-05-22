# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    project config

    :copyright: (c)  2018/5/22 by zwhset.
    :license: OPS, see LICENSE_FILE for more details.
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__)) # 设置基础目录

class Config(object):
    '''配置基础类'''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'TxuvWdN[PYOB2V0yMGn5q4Fk'
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True # 事件自动提交，作者将要剔除，故关闭
    SQLALCHEMY_TRACK_MODIFICATIONS = True # 取消这个报警信息

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    '''开发类'''
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@host:port/db?charset=utf8mb4'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = '' # 替换线上的链接


config = {
    'development' : DevelopmentConfig,
    'production' : ProductionConfig,

    'default' : DevelopmentConfig,
}
