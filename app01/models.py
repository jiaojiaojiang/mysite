from __future__ import unicode_literals
from django.contrib import admin
from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField()


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email')


admin.site.register(User, UserAdmin)

class WX(models.Model):
    bookname = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    des = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    bookid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'wx'

class ZX(models.Model):
    bookname = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    des = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'zx'

class JY(models.Model):
    bookname = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    des = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'jy'

class Libraries(models.Model):
    bookid = models.AutoField(primary_key=True)
    bookname = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    des = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'libraries'