#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Simple database operations """

from flask import g
import sqlite3

DATABASE="catalog3_db" 

def get_db():
    db = getattr(g, "_database", None)
    if not db:
        db = g._database = sqlite3.connect(DATABASE)
    return db

#whatever your fn outputs this fn will format the results
#you don't have to specify the data type
def output_formatter(results: tuple):
    out = {"body": []}
    for result in results:
        res_dict = {}
        res_dict["id"] = result[0]
        res_dict["name"] = result[1]
        res_dict["price"] = result[2]
        res_dict["description"] = result[3]
        res_dict["category"] = result[4]
        res_dict["quantity"] = result[5]
        res_dict["unique_tag"] = result[6]
        res_dict["active"] = result[7]
        out["body"].append(res_dict)

    return out


def scan():
    cursor = get_db().execute("SELECT * FROM product", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results) #formatted results


#sqlite3 '?' = helps prevent a sql injection attack from binding. 
def read(prod_id):
    query = """
        SELECT * 
        FROM product
        WHERE id = ? 
        """
    cursor = get_db().execute(query, (prod_id,))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

#create a string for ea. key/value pairs
#  \" - this is an escape expression to make sure the quote is added in string. 
def update(prod_id, fields: dict):
    field_string = ", ".join(
            "%s=\"%s\"" % (key, val)
                for key, val 
                in fields.items()) 

    query = """
        UPDATE product
        SET %s 
        WHERE id = ?
        """ % field_string
    
    cursor = get_db()
    cursor.execute(query, (prod_id,))
    cursor.commit()
    return True

# METHOD TO DEACTIVATE COL 'active'
def softdelete(prod_id, value):

    if value == 1:
        query = "UPDATE product SET active=FALSE WHERE id=%s" % prod_id
    else:
        query = "UPDATE product SET active=TRUE WHERE id=%s" % prod_id

    cursor = get_db()
    cursor.execute(query)
    cursor.commit()

    return query

def create(name, price, description, category, quantity, unique_tag):
    value_tuple = (name, price, description, category, quantity, unique_tag)
    query = """
            INSERT INTO product (
                name, 
                price,
                description,
                category,
                quantity,
                unique_tag)
            VALUES (?, ?, ?, ?, ?, ?)
            """
    cursor = get_db()
    last_row_id = cursor.execute(query, value_tuple).lastrowid
    cursor.commit()
    return last_row_id #return the automatically generated 'id'

#not recommended because most companies want to keep all code. 
#typically deactivation of columns happens. 
def delete(prod_id):
    query = "DELETE FROM product WHERE id=%s" % prod_id
    cursor = get_db()
    cursor.execute(query, ())
    cursor.commit()
    return True


# ############### Review Table Functions ###################### #
# Output formatter for Reviews table
def review_formatter(results: tuple):
    out = {"body": []}
    for result in results:
        res_dict = {}
        res_dict["id"] = result[0]
        res_dict["prodId"] = result[1]
        res_dict["review"] = result[2]
     
        out["body"].append(res_dict)

    return out
#adding comment to review table 
def create_Review(p_id, body):
    value_tuple = (int(p_id), body)
    query = """
            INSERT INTO reviews (
                idProduct, 
                comment)
            VALUES (?, ?)
            """
    cursor = get_db()
    last_row_id = cursor.execute(query, value_tuple).lastrowid
    cursor.commit()
    return last_row_id #return the automatically generated 'id'

# Fn to return review DB
def read_Review(pid):

    query = """
        SELECT * 
        FROM reviews
        WHERE idProduct = ? 
        """
    cursor = get_db().execute(query, (pid,))
    results = cursor.fetchall()
    cursor.close()
    return review_formatter(results)