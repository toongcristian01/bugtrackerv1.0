from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
# User = settings.AUTH_USER_MODEL
from accounts.models import Role, EmployeeProfile
from simple_history.models import HistoricalRecords

class Type(models.Model):
  type = models.CharField(max_length=100, null=True,blank=True)
  def __str__(self):
    return self.type
class Priority(models.Model):
  priority = models.CharField(max_length=100, null=True,blank=True)
  def __str__(self):
    return self.priority
class Status(models.Model):
  status = models.CharField(max_length=100, null=True,blank=True)
  def __str__(self):
    return self.status


class Project(models.Model):
  name = models.CharField(max_length=200,null=True,blank=True)
  description = models.TextField(null=True,blank=True)
  submission_date = models.DateField(blank=True, null=True)
  assigned_members = models.ManyToManyField(EmployeeProfile)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.name
  def get_absolute_url(self):
    return reverse('bugtracker:project_detail', kwargs={'id': self.id})


class Ticket(models.Model):
  title = models.CharField(max_length=200,null=True,blank=True)
  ticket_description = models.TextField(null=True,blank=True)
  image = models.ImageField(upload_to='ticketimgs/', blank=True, null=True)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  author = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, related_name='tickets', unique=False)
  assign_members = models.ManyToManyField(User, related_name='devs', blank=True)
  type = models.ForeignKey(Type, on_delete=models.CASCADE)
  priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
  status = models.ForeignKey(Status, on_delete=models.CASCADE)
  #assigned = models.BooleanField(default=False)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)
  history = HistoricalRecords(cascade_delete_history=True)
  class Meta:
    ordering = ('-created',)

  def __str__(self):
    return self.title
  @property
  def get_comments(self):
    # Post.reviews.all(), reviews->from Post related name in Review model
    return self.comments.all().order_by('-date')


class Comment(models.Model):
  ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comments')
  name = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
  body = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.body[0:20]


NOTIFICATION_TYPE = (
  ('New Ticket', 'New Ticket'),
)

class Notification(models.Model):
  notif_receiver = models.ManyToManyField(EmployeeProfile, blank=True, related_name="noti_user")
  sender = models.ForeignKey(EmployeeProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name="noti_sender")
  ticket = models.ForeignKey(Ticket, on_delete=models.SET_NULL, null=True, blank=True, related_name="noti_post")
  comment = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True, blank=True, related_name="noti_comment")
  notification_type = models.CharField(max_length=100, choices=NOTIFICATION_TYPE, default="none")
  is_read = models.BooleanField(default=False)
  date = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ('-date',)
  
  def mark_as_read_count(self):
    return self.objects.filter(is_read=True).count()

  @classmethod
  def is_read_query(cls, threshold):
      return cls.objects.filter(value__gt=threshold)