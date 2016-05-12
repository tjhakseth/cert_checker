from django import forms
from .models import Website

class WebsiteInputForm(forms.ModelForm):

    class Meta:
        model = Website
        fields = ('url',)