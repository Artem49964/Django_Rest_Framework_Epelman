from datetime import datetime

from django.core import validators as V
from django.db import models

from apps.autoparks.models import AutoParkModel
from apps.core.enums.regex_enum import RegExEnum
from apps.core.models import BaseModel

from .choices.body_type_choices import BodyTypeChoices
from .managers import CarManager


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20,validators=(
        V.RegexValidator(RegExEnum.BRAND.pattern, RegExEnum.BRAND.msg),))

    price = models.IntegerField(validators=(
        V.MinValueValidator(0), V.MaxValueValidator(1000000)))

    year = models.IntegerField(validators=(
        V.MinValueValidator(1990), V.MaxValueValidator(datetime.now().year),))



    body = models.CharField(max_length=11, choices=BodyTypeChoices.choices)
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')

    objects = CarManager()
    

