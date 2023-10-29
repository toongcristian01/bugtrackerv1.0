
from .models import EmployeeProfile

def menu_links(request):
  links = EmployeeProfile.objects.all()
  return dict(links=links)