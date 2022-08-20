from django import forms
from .models import webseries

class seriesform(forms.ModelForm):
    class Meta:
        model= webseries
        fields=['name','img','desc','year']