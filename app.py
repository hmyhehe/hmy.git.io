#!/usr/bin/python3

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        name = request.form['id']
        password = request.form['pwd']
        if name == 'zhangsan' and password == '123'
            return render_template("welcome.html",name = name)
        else:
            return render_template("login.html")
