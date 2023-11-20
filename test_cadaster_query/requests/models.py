from django.db import models


class CadasterRequest(models.Model):
    cadaster_number = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    result = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
