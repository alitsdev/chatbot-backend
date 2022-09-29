from django.contrib import admin
from .models import ChatUser, AssistanceRequest

admin.site.register(ChatUser)
admin.site.register(AssistanceRequest)