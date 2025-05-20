from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'capacity', 'created_by')
    search_fields = ('title', 'description')
    list_filter = ('event_date',)
    filter_horizontal = ('attendees',)