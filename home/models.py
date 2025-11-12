# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    user1 = models.CharField(max_length=255, null=True, blank=True)
    user2 = models.TextField(max_length=255, null=True, blank=True)
    user4 = models.IntegerField(null=True, blank=True)
    user5 = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Product(models.Model):

    #__Product_FIELDS__
    field1 = models.CharField(max_length=255, null=True, blank=True)
    field2 = models.TextField(max_length=255, null=True, blank=True)
    field3 = models.BooleanField()
    field4 = models.IntegerField(null=True, blank=True)
    field5 = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Client(models.Model):

    #__Client_FIELDS__
    clientnom = models.CharField(max_length=255, null=True, blank=True)
    clientprénom = models.CharField(max_length=255, null=True, blank=True)
    date de naissance = models.DateTimeField(blank=True, null=True, default=timezone.now)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE)

    #__Client_FIELDS__END

    class Meta:
        verbose_name        = _("Client")
        verbose_name_plural = _("Client")



#__MODELS__END
