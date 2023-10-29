from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.models import Group
from django.urls import reverse
from django.conf import settings
# User = settings.AUTH_USER_MODEL

class Role(models.Model):
  role = models.CharField(max_length=50)
  def __str__(self):
    return self.role


# class CustomUserRoleChoices(AbstractUser):
#   ROLE_CHOICES = (
#       (1, 'Admin'),
#       (2, 'Tester'),
#       (3, 'Developer'),
#   )
#   role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=1)

#   @property
#   def tester_key(self):
#     return self.ROLE_CHOICES[1][0]
#   @property
#   def developer_key(self):
#     return self.ROLE_CHOICES[2][0]
#   @property
#   def tester_value(self):
#     return self.ROLE_CHOICES[1][1]
#   @property
#   def developer_value(self):
#     return self.ROLE_CHOICES[2][1]


class EmployeeProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  employee_id = models.CharField(max_length=128, blank=True)
  first_name = models.CharField(max_length=200, blank=True)
  last_name = models.CharField(max_length=200, blank=True)
  email = models.EmailField(max_length=200, blank=True)
  role = models.ForeignKey(Role,on_delete=models.CASCADE)
  avatar = models.ImageField(default='avatar.jpg', upload_to='avatars/', blank=True)
  phone_number = models.CharField(max_length=50, blank=True)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)
  class Meta:
    ordering = ('-created',)
  #profile detail slug
  def get_absolute_url(self):
    return reverse('accounts:profile-detail-view', kwargs={'slug': self.slug})
  def __str__(self):
    return self.first_name + " " + self.last_name