from django.db import models


class AuthPhone(models.Model):
    seq = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=30, null=False, unique=True)
    auth_number = models.IntegerField(null=False)
    is_success = models.BooleanField(default=False)
    create_dt = models.DateField(auto_now_add=True)
