#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Simple python requests tests for visual confirmation. These aren't unit tests. 
"""

import requests
from pprint import pprint

def test_scan():
    resp = requests.get("http://127.0.0.1:5000/products")
    pprint(resp.json())

def test_read():
    resp = requests.get("http://127.0.0.1:5000/products/1")
    pprint(resp.json())

def test_create():
    sample = {"name": "banana", "price": 1.0, "description": "Yellow", "category": "banana", "quantity": 500, "unique_tag": "lifting",}
    resp = requests.post("http://127.0.0.1:5000/products", json=sample)
    pprint(resp.json())

def test_update():
    sample = {"name": "banana", "price": 2.0}
    resp = requests.put("http://127.0.0.1:5000/products/2", json=sample)
    pprint(resp.json())


if __name__=="__main__":
    test_scan()
    test_read()
    test_create()
    test_update()


