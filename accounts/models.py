from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [
        ('normal', 'کاربر عادی'),
        ('member', 'عضو انجمن'),
        ('admin', 'مدیر انجمن'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='normal')
    