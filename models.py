from django.db import models
from django.contrib.auth.models import User
import datetime

class Item(models.Model):
    name = models.CharField(max_length=56)
    description = models.CharField(max_length=256)
    once_a_day = models.BooleanField()

    def __unicode__(self):
        return '%s: %s' % (self.name, self.description,)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

class Order(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField(default=datetime.date.today)
    item = models.ForeignKey(Item)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __unicode__(self):
        return "%d %s(s) on %s."% (self.quantity, self.item.name, self.date,)
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ["date"]
