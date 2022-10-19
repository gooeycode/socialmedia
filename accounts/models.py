from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    tagline = models.CharField(max_length=200, null='', blank=True)
    notifications = models.BooleanField(name="notifications", default=True, help_text="notifications are automatically set to")





# Create your models here.
