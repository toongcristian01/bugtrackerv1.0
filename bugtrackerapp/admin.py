from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Type,Priority,Status,Project,Ticket, Comment

admin.site.register(Type)
admin.site.register(Priority)
admin.site.register(Status)
admin.site.register(Project)
admin.site.register(Ticket, SimpleHistoryAdmin)
admin.site.register(Comment)
