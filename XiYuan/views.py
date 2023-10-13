from XiYuan import app
from flask import render_template,request,url_for,redirect,flash

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/market')
def market():
    return render_template('market.html')

@app.route('/plant')
def plant():
    return render_template('plant.html')

@app.route('/accommodation')
def accommodation():
    return render_template('accommodation.html')

@app.route('/technology')
def technology():
    return render_template('technology.html')