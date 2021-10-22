from django.contrib import admin
from apps.send_email.models import MessageSender

# Register your models here.
admin.site.register(MessageSender)
