from XiYuan import app
from flask import render_template,request,url_for,redirect,flash

@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
    if request.method=='POST':
        flash('预约暂未开放')
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/market')
def market():
    return render_template('market.html')

@app.route('/plant',methods=['GET','POST'])
def plant():
    if request.method=='POST':
        flash('预约暂未开放')
        return redirect(url_for('plant'))
    return render_template('plant.html')

@app.route('/accommodation')
def accommodation():
    return render_template('accommodation.html')

@app.route('/technology',methods=['GET','POST'])
def technology():
    if request.method=='POST':
        flash('预约暂未开放')
        return redirect(url_for('technology'))
    return render_template('technology.html')