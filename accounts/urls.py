from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
  path('', views.login_view, name='login_view'),
  path('logout_view', views.logout_view, name="logout_view"),
  path('accounts/register', views.register_view, name='register_view'),
]