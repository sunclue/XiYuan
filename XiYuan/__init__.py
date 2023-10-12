import os
import sys

from flask import Flask

app=Flask(__name__)

app.config['SECRET_KEY']=os.getenv('SECRET_KEY','dev')

from XiYuan import views,commands