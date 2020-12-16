#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Simple database operations """
# """ Magic python file that tells python that it should be treated as a module """

from flask import Flask
from flask_bootstrap import Bootstrap


STATIC_DIR = ('/static/')

app = Flask(__name__, static_folder=STATIC_DIR)
Bootstrap(app)
app.config["SECRET_KEY"] = "MYSUPERSECRETSTRING"

from app import routes