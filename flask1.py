# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 16:48:09 2018

@author: ASUS
"""
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'hello'
@app.route('/user/<name>')
def user(name):
    return 'hello,%s' % name
if __name__ == '__mian__':
    app.run()
    
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return 'hello'
if __name__ == '__name__':
    app.run()





# gfsdgsfhg大锅饭的后果














    
