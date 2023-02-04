from django.db import models


class Customer(models.Model):
    email = models.EmailField(primary_key=True)
    nick_name = models.CharField(max_length=20)
    password = models.TextField()
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=30)
    create_dt = models.DateField(auto_now_add=True)
