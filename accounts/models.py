import os
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.models import Group
from django.urls import reverse
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont
# User = settings.AUTH_USER_MODEL

def generate_initials_image(username, initials, output_dir='media/initials_images'):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Create a blank image
    width, height = 100, 100
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Choose a font and size
    font = ImageFont.load_default()
    font_size = 20

    # Calculate the position to center the initials
    # text_width, text_height = draw.textsize(initials, font)
    # x = (width - text_width) / 2
    # y = (height - text_height) / 2

    # Draw the initials on the image
    draw.text((220,35), initials, fill="black", font=font)

    # Save the image with a filename based on the username
    image_path = os.path.join(output_dir, f"initials_{username}.png")
    image.save(image_path)

    return image_path

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
  avatar = models.ImageField(default='avatar.png', upload_to='avatars/', blank=True)
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

  def get_initials(self):
    initials = ''.join([name[0].upper() for name in self.user.get_full_name().split() if name])
    return initials
  
  def get_fullname(self):
    return self.first_name + " " + self.last_name