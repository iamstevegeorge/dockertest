# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 13:20:38 2020

@author: 756097
"""

from flask import Flask,jsonify

app=Flask(__name__)

@app.route("/")
def extract():
    
    return ("Hello World")


if __name__=='__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)