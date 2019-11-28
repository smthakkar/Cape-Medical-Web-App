from django.core.exceptions import PermissionDenied
from Order.models import Teamsettings1

def user_is_staff(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_staff:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied


    wrap.__doc__ = function.__doc__
    # wrap.__name__ = function.__name__
    return wrap