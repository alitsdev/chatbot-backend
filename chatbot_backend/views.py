from .models import AssistanceRequest, ChatUser
from .serializers import AssistanceRequestSerializer, ChatUserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def chatUser_list(request, format=None):

    if request.method == 'GET':
        chatUsers = ChatUser.objects.all()
        serializer = ChatUserSerializer(chatUsers, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ChatUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            ChatUser.send_email(request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def assistance_request(request, format=None):

    if request.method == 'GET':
        requests = AssistanceRequest.objects.all()
        serializer = AssistanceRequestSerializer(requests, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = AssistanceRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('hola')
            print(request.data['topic'])
            if request.data['topic'] == 'sales':
                print('sales')
            if request.data['topic'] == 'pricing':
                print('pricing')
            if request.data['topic'] == 'shipping':
                print('shipping')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
