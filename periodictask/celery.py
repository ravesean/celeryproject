from __future__ import absolute_import
from celery import Celery

#Configure celery.
app = Celery('periodictask',
                broker='sqla+postgresql://postgres:root@localhost/celery-db',
                backend='db+postgresql://postgres:root@localhost/celery-db',
                include=['periodictask.tasks'])
