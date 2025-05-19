# forms.py
from django import forms
from .models import Announcement

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'image', 'status']  # datetime فیلدهای اتومات هستن و نیازی به ورودی ندارن
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'متن اعلان'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }