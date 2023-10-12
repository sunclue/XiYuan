from XiYuan import app
from flask import render_template,request,url_for,redirect,flash

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/market')
def market():
    return render_template('market.html')