# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from flask import Flask

app=Flask(__name__)

@app.route('/')
def add():
    a=10
    b=20
    return str(a+b)

if __name__=='__main__':
    app.run()
    

