# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    程序主目录

    :copyright: (c)  2018/5/22 by zwhset.
    :license: OPS, see LICENSE_FILE for more details.
"""

from flask import Flask, Blueprint, render_template, request, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):

    # laoding config
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # init app
    db.init_app(app)

    # register route and define error page.
    from main.views import index_page

    app.register_blueprint(index_page)

    return app