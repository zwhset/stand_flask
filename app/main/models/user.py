# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    Example modles

    :copyright: (c)  2018/5/22 by zwhset.
    :license: OPS, see LICENSE_FILE for more details.
"""

from datetime import datetime

from app import db

class User(db.Model):
    '''用户表'''

    __tablename__ = 'users' # 表名

    __table_args__ = { # 表参数
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }

    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # id
    username = db.Column(db.VARCHAR(55), unique=True, nullable=False) # 用户名
    password = db.Column(db.VARCHAR(125), nullable=False) # 密码
    email = db.Column(db.VARCHAR(255), unique=True, nullable=True) # 邮箱
    create_time = db.Column(db.DateTime, default=datetime.now)  # 创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 更新时间

    def __init__(self, username, password, email, create_time, update_time):
        self.username = username
        self.password = password
        self.email = email
        self.create_time = create_time
        if not update_time:
            self.update_time = datetime.now()
        else:
            self.update_time = update_time

    def __repr__(self):
        return '<User %s>' % self.username

    def to_dict(self):
        data = dict(id=self.id,
                    username=self.username,
                    password=self.password,
                    email=self.email,
                    create_time=self.create_time,
                    update_time=self.update_time)
        return data

    def save(self):
        '''定制属性方法'''
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        '''定制更新方法'''
        db.session.commit()
        return self

