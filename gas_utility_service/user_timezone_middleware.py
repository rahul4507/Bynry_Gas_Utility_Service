# custom_middleware.py

from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

class UserTimezoneMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            user_timezone = request.user.timezone
            if user_timezone:
                timezone.activate(user_timezone)
            else:
                timezone.deactivate()
        else:
            timezone.deactivate()