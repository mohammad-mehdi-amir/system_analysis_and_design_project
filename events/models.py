from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    event_date = models.DateTimeField(auto_now_add=True)
    capacity = models.IntegerField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_events')
    attendees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='attended_events', blank=True)

    def __str__(self):
        return self.title