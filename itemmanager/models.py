from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

from rest_framework.authtoken.models import Token

# Create your models here.


class Item(models.Model):
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=400, unique=True)
    insprice = models.FloatField(default=0)
    taxrate = models.CharField(max_length=3, default='B')
    synced = models.IntegerField(default=0)
    itemclscode = models.CharField(max_length=30)
    pckagunitcode = models.CharField(max_length=20, default='NT')
    package = models.IntegerField(default=1)
    qtyunitycode = models.CharField(max_length=20, default='U')
    barcode = models.CharField(max_length=30)
    itemtypcode = models.CharField(max_length=10, default='2')
    nationcode = models.CharField(max_length=20, default='RW')
    vsdcsent = models.CharField(max_length=20, default='N')
    standardname = models.CharField(max_length=400)
    batchno = models.CharField(max_length=20)
    registbranchid = models.CharField(max_length=10)
    dftprice = models.FloatField(default=0)
    grp1price = models.FloatField(default=0)
    grp2price = models.FloatField(default=0)
    grp3price = models.FloatField(default=0)
    grp4price = models.FloatField(default=0)
    grp5price = models.FloatField(default=0)
    addinfo = models.CharField(max_length=25)
    saftyqty = models.FloatField(default=0)
    insuranceapplicable = models.CharField(max_length=4, default='N')
    usedorunused = models.CharField(max_length=4, default='N')
    lastreqdate = models.CharField(max_length=30)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
