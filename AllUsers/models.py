from datetime import datetime
import os
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.http import HttpRequest
from django.shortcuts import render


import csv
from django.http import HttpResponse



class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150,unique=True, null=False)
    role = models.CharField(blank=True, null=True, max_length=10, default="Resident")  # Add the age field to the custom user model
    HouseUnit = models.CharField(blank=True, null=True, max_length=10, default="")
    ParkingLot = models.CharField(blank=True, null=True, max_length=10, default="")

    class Meta:
        default_related_name = 'custom_users'
        permissions = [('can_do_something', 'Can do something')]

    def __str__(self):
        return str(self.username)

    groups = models.ManyToManyField (
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_user_groups',  # Change related_name to avoid clashes
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_permissions'  # Change related_name to avoid clashes
    )

    def delete(self, *args, **kwargs):
        self.groups.clear()
        super().delete(*args, **kwargs)

@receiver(pre_save, sender=CustomUser)
def update_house_unit(sender, instance, **kwargs):
    if instance.role == 'Resident':
        instance.HouseUnit = 'PPAP'
    else:
        instance.HouseUnit = None


@receiver(pre_delete, sender=CustomUser)
def remove_user_from_groups(sender, instance, **kwargs):
    instance.groups.clear()


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Additional profile fields like profile picture, bio, etc.



class MonthField(models.DateField):
    def pre_save(self, model_instance, add):
        # Set day to 01 and year to a fixed value (e.g., 2000)
        value = getattr(model_instance, self.attname)
        value = datetime.strptime(f"{value.month:02d}-01", "%m-%d").date()
        setattr(model_instance, self.attname, value)
        return value



class UserPaymentModel(models.Model): #User's invoice
    InvoiceID = models.AutoField(primary_key=True, unique=True)
    userID = models.ForeignKey(CustomUser, blank=True, null=True, on_delete = models.CASCADE)
    PaymentAmount = models.CharField(max_length=20, default="0")
    InvoiceDate = models.DateField(auto_now=True)
    InvoiceTime = models.TimeField(auto_now=True)
    InvoiceImage = models.ImageField(null=True, blank=True, upload_to="payment/", )
    paid = models.BooleanField("paid?")
    InvoiceMonth = MonthField()

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payment'
  

    def __int__(self):
        return self.InvoiceID
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Checking if it's a new instance
            last_record = UserPaymentModel.objects.order_by('-InvoiceID').first()
            if last_record:
                self.InvoiceID = last_record.InvoiceID + 1
            else:
                self.InvoiceID = 1023000  # Starting from 10001 for the first record

        super().save(*args, **kwargs)

class UploadPaymentModel(models.Model): #user upload thir receipt
    PaymentID = models.AutoField(primary_key=True, unique=True)
    PaymentImage = models.FileField(null=True, blank=True, upload_to='payment/Inovice/')
    username = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Payment Upload'
        verbose_name_plural = 'Payment Upload'

    def __int__(self):
        return self.PaymentID    

    def save(self, *args, **kwargs):
        if not self.pk:  # Checking if it's a new instance
            last_record = UserPaymentModel.objects.order_by('-InvoiceID').first()
            if last_record:
                self.InvoiceID = last_record.InvoiceID + 1
            else:
                self.InvoiceID = 52430000  # Starting from 10001 for the first record

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the associated payment image file when the instance is deleted
        if self.PaymentImage:
            if os.path.isfile(self.PaymentImage.path):
                os.remove(self.PaymentImage.path)

        self.userID = kwargs.pop('user', None)
        super().delete(*args, **kwargs)

    

        





