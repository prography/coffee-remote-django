from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pickuptime = models.IntegerField()
    ordernumber = models.IntegerField()

