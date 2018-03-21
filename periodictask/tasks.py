from __future__ import absolute_import
from periodictask.celery import app
import datetime
from celery.decorators import periodic_task
from datetime import timedelta
from celery.decorators import task

@task()
def longtime_add(x, y):
    print('long time task begins')
    # sleep 5 seconds
    #time.sleep(5)
    print('long time task finished')
    return x + y

@periodic_task(run_every=datetime.timedelta(minutes=1))
def print_name():
        print("Welcome to celery scheduler")
