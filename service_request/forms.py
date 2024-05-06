from django import forms
from django.utils import timezone
import pytz  
import datetime
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):

    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = ServiceRequest
        fields = ['type', 'description', 'attachment', 'requestdate_in_local']