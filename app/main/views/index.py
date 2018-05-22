# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    Example index page.

    :copyright: (c)  2018/5/22 by zwhset.
    :license: OPS, see LICENSE_FILE for more details.
"""

from app import Blueprint, jsonify

from app.main.models.user import User

index_page = Blueprint('index_page', __name__)

@index_page.route('/')
def index():
    return 'This is example index page.'

@index_page.route('/users')
def users():
    user_list = [ user.to_dict() for user in User.query.all() if user ]
    return jsonify(user_list)

