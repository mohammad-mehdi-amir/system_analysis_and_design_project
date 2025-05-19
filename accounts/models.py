from django.db import models

# Create your models here.
class User(models.Model):
    ROLE_CHOICES = [
        ('normal', 'کاربر عادی'),
        ('member', 'عضو انجمن'),
        ('admin', 'مدیر انجمن'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='normal')
