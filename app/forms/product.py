#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Product Form """


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    name = StringField("What is the sport gear name?", validators=[DataRequired()])
    price = StringField("How much does it cost?", validators=[DataRequired()])
    description = StringField("Enter a description of the gear: ", validators=[DataRequired()])
    category = StringField("Is this gear for a Team or Inidividual sport?", validators=[DataRequired()])
    quantity = StringField("How many of this item are sold at one time?", validators=[DataRequired()])
    unique_tag = StringField("What sport is this gear intended for?", validators=[DataRequired()])
    submit = SubmitField("Submit")