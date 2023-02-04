from django.db import models


class AuthPhone(models.Model):
    phone = models.CharField(max_length=30, primary_key=True)
    auth_number = models.IntegerField(default=0)
    is_success = models.BooleanField(default=False)
