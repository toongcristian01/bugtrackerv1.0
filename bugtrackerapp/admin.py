from django.contrib import admin

from .models import Type,Priority,Status,Project,Ticket, Comment

admin.site.register(Type)
admin.site.register(Priority)
admin.site.register(Status)
admin.site.register(Project)
admin.site.register(Ticket)
admin.site.register(Comment)