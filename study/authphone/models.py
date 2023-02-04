from django.db import models


class AuthPhone(models.Model):
    phone = models.CharField(max_length=30, primary_key=True)
    auth_number = models.IntegerField(null=False)
    is_success = models.BooleanField(default=False)
    create_dt = models.DateField(auto_now_add=True)
