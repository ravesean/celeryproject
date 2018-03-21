from django.contrib import admin
from kombu.transport.sqlalchemy import models as kombu_models
site.register(kombu_models.Message)
