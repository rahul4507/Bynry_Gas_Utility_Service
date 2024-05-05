from django import forms
from django.utils import timezone
import pytz  
from .models import ServiceRequest
import datetime

class ServiceRequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = ServiceRequest
        fields = ['type', 'description', 'attachment', 'requestdate_in_local', 'requestdate_in_utc']

    def clean_requestdate_in_local(self):
        
        # timezone_info = requestdate_in_local.tzinfo
        # print("Timezone information:", timezone_info)


        requestdate_in_local = self.cleaned_data.get('requestdate_in_local')
        # requestdate = datetime.datetime.strptime(requestdate, '%Y-%m-%d %H:%M:%S')
      
        user_timezone = pytz.timezone(self.request.user.timezone)
        
        requestdate_in_local=requestdate_in_local.astimezone(user_timezone)
        requestdate_in_local=requestdate_in_local.replace(tzinfo=None)
        
        print(requestdate_in_local)
        return requestdate_in_local
