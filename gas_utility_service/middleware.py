import pytz
import datetime

class AddTimeToDateTimeFieldsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
       
            if hasattr(request, 'user') and request.user.is_authenticated:
                user_timezone = pytz.timezone(request.user.timezone)
                
                mutable_post = request.POST.copy()
                
                for key, value in request.POST.items():
                    try:
                        datetime_value = datetime.datetime.strptime(value, '%m/%d/%Y')
                        datetime_value = user_timezone.localize(datetime_value)
                        current_time_in_user_timezone = datetime.datetime.now(user_timezone).time()
                        datetime_value = datetime.datetime.combine(datetime_value.date(), current_time_in_user_timezone)
                        mutable_post[key] = datetime_value.strftime('%Y-%m-%d %H:%M:%S')  
                    except ValueError:
                        pass  
                
                request.POST = mutable_post
        
            response = self.get_response(request)
            return response
