from django.db import models

# Create your models here.


class Numeric(models.Model):
    numa = models.FloatField()
    numb = models.FloatField()
    result = models.FloatField(blank=True)