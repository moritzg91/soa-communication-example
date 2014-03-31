from celery import Celery

BROKER_URL = 'amqp://guest:guest@localhost:5672//'
celery = Celery('tasks', broker=BROKER_URL, backend='amqp')

@celery.task(name='mult')
def mult(lhs,rhs):
	return lhs*rhs