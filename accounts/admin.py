from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
@admin.register(User)
class CustomuserAdmin(UserAdmin):
    list_display =['email','username','role']
    
    fieldsets =  (
        ('Custom Fields', {
            'fields': ('role',)
        }),
    )+UserAdmin.fieldsets 
