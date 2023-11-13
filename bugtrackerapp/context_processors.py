from bugtrackerapp.models import Notification

def my_context_processor(request):
  try:
    notification = Notification.objects.filter(notif_receiver=request.user.profile)
    notification_count = Notification.objects.filter(notif_receiver=request.user.profile).filter(is_read=False).count()
  except:
    notification = None
  return {
    'notification':notification,
    'notification_count':notification_count,
  }