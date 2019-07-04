from django.db import models
from django.utils import timezone


class Order(models.Model):
    unique_id = models.CharField(max_length=30, default=0)
    created_at = models.DateTimeField(default=timezone.now)
    price = models.IntegerField()
    # pickuptime = models.IntegerField()
    order = models.CharField(max_length=50)



# unique_id : 아이디(string)
# price : 총 가격(int)
# pickuptime : 5 또는 10 (int)
# order : 메뉴id,수량;(string) ex> "3,5;4,1;"

# pickup -

# admin
