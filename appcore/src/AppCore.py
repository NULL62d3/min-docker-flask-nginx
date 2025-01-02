#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "index"


@app.route('/AppCore/sayHello', methods=['GET'])
def sayHello():
    return f"sayHello: Hello!"

@app.route('/AppCore/sayName/<name>', methods=['GET'])
def sayName(name):
    return f"sayName: Hello! {name}"


