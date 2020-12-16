#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Review Product Form """


from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired
from wtforms import validators


class ProductReview(FlaskForm):

    # Product Name
    id = RadioField(choices=[], validators=[DataRequired()])

    # Feedback
    body = TextAreaField("Tell Us Your Thoughts", [validators.optional(), validators.length(max=200)])

    # Submit Review
    submit = SubmitField("Submit")

