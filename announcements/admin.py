# admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Announcement

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title',  'datetime_add', 'image_preview')
    list_filter = ('datetime_add',)
    search_fields = ('title', 'content')
    readonly_fields = ('datetime_add', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius: 4px;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Preview'