# models.py
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
class Article(models.Model):
    STATUS_CHOICES = [
        ('pending', 'در حال بررسی'),
        ('approved', 'قبول شده'),
        ('rejected', 'رد شده'),
    ]

    title = models.CharField(max_length=255)
    text = models.TextField()
    datetime_add = models.DateTimeField(auto_now_add=True)
    datetime_edit = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return self.title