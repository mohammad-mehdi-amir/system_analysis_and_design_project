from django.db import models

# Create your models here.
class Announcement(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    image = models.ImageField(upload_to='announcements/', null=True, blank=True)
    datetime_add = models.DateTimeField(auto_now_add=True,verbose_name=' add date')
    datetime_edit = models.DateTimeField(auto_now=True,verbose_name='edite date')
    status = models.BooleanField(default=True,verbose_name='status')
    def __str__(self):
        return self.title