from django.db import models

from apps.core.models import BaseModel

from .managers import AutoParkManager


class AutoParkModel(BaseModel):
    class Meta:
        db_table = 'autoparks'

    name = models.CharField(max_length=20)

    objects = AutoParkManager()


