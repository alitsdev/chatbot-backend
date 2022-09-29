from rest_framework import serializers
from .models import ChatUser
from .models import AssistanceRequest

class ChatUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatUser
        fields = ['id', 'name', 'email', 'phoneNumber']
class AssistanceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssistanceRequest
        fields = ['id', 'topic', 'text']