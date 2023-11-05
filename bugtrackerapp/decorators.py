from functools import wraps
from django.http import HttpResponseForbidden
from accounts.models import EmployeeProfile, Role

def role_required(allowed_roles):
  def decorator(view_func):
      @wraps(view_func)
      def _wrapped_view(request, *args, **kwargs):
          if request.user.is_authenticated:
            #if Role.objects.filter(role__in=allowed_roles).exists():
            if request.user.profile.role.role in allowed_roles:
              return view_func(request, *args, **kwargs)
          return HttpResponseForbidden("You don't have permission to access this page.")
      return _wrapped_view
  return decorator