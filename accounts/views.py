from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Role,EmployeeProfile
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from bugtrackerapp.decorators import role_required


def login_view(request):
  role = Role.objects.all()
  profile = EmployeeProfile.objects.all()
  is_admin_login = False
  is_tester_login = False
  is_developer_login = False

  if request.method == 'POST':
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None and user.profile.role.role == "Admin":
      is_admin_login = True
      login(request, user)
      messages.success(request, f'Welcome {request.user.profile}')
      #return redirect('bugtracker:admin_dashboard')
      return redirect('bugtracker:home')
    elif user is not None and user.profile.role.role == 'Tester':
        is_tester_login = True
        login(request, user)
        messages.success(request, f'Welcome {request.user.profile}')
        #return redirect('bugtracker:tester_dashboard')
        return redirect('bugtracker:home')
    elif user is not None and user.profile.role.role == 'Developer':
        is_developer_login = True
        login(request, user)
        messages.success(request, f'Welcome {request.user.profile}')
        #return redirect('bugtracker:developer_dashboard')
        return redirect('bugtracker:home')
    else:
      messages.error(request, 'There was An Error Loggin In, Try Again.')
      return redirect('accounts:login_view')
  context = {
    'is_admin_login':is_admin_login,
    'is_tester_login':is_tester_login,
    'is_developer_login':is_developer_login,
  }
  return render(request, 'accounts/login.html', context)

# def login_view(request):
#   if request.method == 'POST':
#     username = request.POST["username"]
#     password = request.POST["password"]
#     user = authenticate(request, username=username, password=password)
#     if user is not None and user.role == 1:
#         login(request, user)
#         return redirect('bugtracker:admin_dashboard')
#     elif user is not None and user.role == 2:
#         login(request, user)
#         return redirect('bugtracker:tester_dashboard')
#     elif user is not None and user.role == 3:
#         login(request, user)
#         return redirect('bugtracker:developer_dashboard')
#     else:
#       messages.error(request, 'There was An Error Loggin In, Try Again.')
#       return redirect('accounts:login_view')
#   else:
#     return render(request, 'accounts/login.html', {})


@login_required(login_url="/")
@role_required(allowed_roles=["Admin"])
def register_view(request):
  # role = CustomUserRoleChoices()
  if request.method == 'POST':
      form = RegisterForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect('accounts:login_view')
  else:
      form = RegisterForm()
      
  return render(request, 'accounts/register.html', {'form': form})

@login_required(login_url="/")
def logout_view(request):
  logout(request)
  messages.warning(request, 'You Were Logged Out!')
  return redirect('accounts:login_view')
