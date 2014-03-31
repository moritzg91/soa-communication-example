from flask import render_template, request
from celery import Celery
from app import app

BROKER_URL = 'amqp://guest:guest@localhost:5672//'
celery = Celery('tasks2', broker=BROKER_URL, backend='amqp')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/multiply',methods=['POST'])
def multiply():
	lhs = float(request.form['lhs'])
	rhs = float(request.form['rhs'])
	return str(celery.send_task("mult", args=[lhs,rhs]).get())