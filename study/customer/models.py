from django.db import models


class Customer(models.Model):
    seq = models.AutoField(primary_key=True)
    email = models.EmailField(null=False, unique=True)
    nick_name = models.CharField(max_length=20, null=False, unique=True)
    password = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=20, null=False)
    phone = models.CharField(max_length=30, null=False, unique=True)
    create_dt = models.DateField(auto_now_add=True)
