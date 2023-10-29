from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ticket, Project, Comment
from accounts.models import EmployeeProfile

class ManageRoleAssignment(forms.ModelForm):
  class Meta:
    model = EmployeeProfile
    fields = ['user', 'role']
    labels = {
    'user': 'User',
    'role': 'Role',
  }
    widgets = {
    'user': forms.Select(attrs={'class':'form-control'}),
    'role': forms.Select(attrs={'class':'form-control'}),
    }

class EditManageRoleAssignment(forms.ModelForm):
  class Meta:
    model = EmployeeProfile
    fields = ('role',)
    labels = {
    'role': 'Role',
  }
    widgets = {
    'role': forms.Select(attrs={'class':'form-control'}),
    }


class CreateProjectFormAdmin(forms.ModelForm):
  class Meta:
    model = Project
    fields = ('name','description', 'submission_date', 'assigned_members')
    labels = {
    'name': 'Name',
    'description': 'Description',
    'submission_date': 'Submission Date',
    'assigned_members': 'Assign Members',
  }
    widgets = {
    'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Name'}),
    'description': forms.Textarea(attrs={'class':'form-control', 'style':'resize:none;', 'rows':10, 'cols': 40,  'placeholder': 'Description'}),
    'submission_date': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Submission Date', 'type': 'date'}),
    'assigned_members': forms.CheckboxSelectMultiple()

    }

class EditProjectFormAdmin(forms.ModelForm):
  class Meta:
    model = Project
    fields = '__all__'


class CreateTicketForm(forms.ModelForm):
  class Meta:
    model = Ticket
    fields = ('title', 'ticket_description', 'image', 'project', 'author', 'assign_members', 'type', 'priority', 'status')
    labels = {
    'title': 'Title',
    'ticket_description': 'Description',
    'image': 'Image',
    'project': 'Project',
    'author': 'Author',
    'assign_members': 'Assign Members',
    'type': 'Type',
    'priority': 'Priority',
    'status': 'Status',
  }
    widgets = {
    'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Name'}),
    'ticket_description': forms.Textarea(attrs={'class':'form-control', 'style':'resize:none;', 'rows':10, 'cols': 40,  'placeholder': 'Description'}),
    'image': forms.FileInput(),
    'project': forms.Select(attrs={'class':'form-control'}),
    'author': forms.Select(attrs={'class':'form-control'}),
    'assign_members': forms.CheckboxSelectMultiple(),
    'type': forms.Select(attrs={'class':'form-control'}),
    'priority': forms.Select(attrs={'class':'form-control'}),
    'status': forms.Select(attrs={'class':'form-control'}),
    }


class EditTicketForm(forms.ModelForm):
  class Meta:
    model = Ticket
    fields = '__all__'
    exclude = ('updated', 'created', 'project', 'author')

class CommentForm(forms.ModelForm):
  #body = forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder': 'Enter Comment'}), required=False)
  class Meta:
    model = Comment
    fields = ('body',)
    labels = {
      'body': '',
    }
    widgets = {
      'body': forms.Textarea(attrs={'class':'form-control', 'style':'resize:none;', 'rows':4, 'cols': 50}),
    }



