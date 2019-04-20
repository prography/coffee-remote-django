from django.db import models
from django.utils import timezone


class Order(models.Model):
    unique_id = models.CharField(max_length=30, default=0)
    created_at = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pickuptime = models.IntegerField()
    ordernumber = models.IntegerField()

