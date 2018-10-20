from __future__ import absolute_import
from celery import Celery

app = Celery('knn-celery', broker='amqp://guest:guest@rabbitmq:5672/guest',
             backend='rpc://', include=['knn.tasks'])
