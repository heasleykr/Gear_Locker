#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Product Form """


from flask_wtf import FlaskForm
from wtforms import SubmitField
# from wtforms import SubmitField, QuerySelectField

class DeleteProduct(FlaskForm):
    # id = QuerySelectField.('prod_id', validators=[Required()])
    submit = SubmitField("Delete")

class ActivateProduct(FlaskForm):
    # id = 
    submit = SubmitField("Un-Delete")