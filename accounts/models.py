from django.contrib.auth.models import User
from django.db import models

from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    level = models.IntegerField(default=1)

    phone_number = models.CharField(max_length=100,blank=True)

