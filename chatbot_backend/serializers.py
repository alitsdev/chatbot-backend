from rest_framework import serializers
from .models import ChatUser

class ChatUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatUser
        fields = ['id', 'name', 'email', 'phoneNumber']