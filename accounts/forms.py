from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import Role

class RegisterForm(UserCreationForm):
  #role = forms.ChoiceField(choices=CustomUserRoleChoices.ROLE_CHOICES)
  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    labels = {
    'username': 'Username',
    'first_name': 'First Name',
    'last_name': 'Last name',
    'email': 'Email Address',
    'password1': 'Password',
    'password2': 'Confirm Password',
  }
    widgets = {
    'username': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Username'}),
    'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}),
    'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}),
    'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email Address'}),
    }

    def __init__(self, *args, **kwargs):
      super(RegisterForm, self).__init__(*args, **kwargs)
      self.fields['password1'].widget.attrs = {'class': 'form-control'}
      self.fields['password2'].widget.attrs = {'class': 'form-control'}
# class EditProfileForm(forms.ModelForm):
#   avatar = forms.ImageField(widget=forms.FileInput)
#   class Meta:
#     model = EmployeeProfile
#     fields = ('employee_id', 'first_name', 'last_name', 'email', 'role', )



