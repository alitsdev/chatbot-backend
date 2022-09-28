from .models import ChatUser
from .serializers import ChatUserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def chatUser_list(request, format=None):

    if request.method == 'GET':
        #get all the drinks
        drinks = ChatUser.objects.all()
        #serialize them
        serializer = ChatUserSerializer(drinks, many=True)
        #return json
        #return JsonResponse({'drinks': serializer.data})
        return Response(serializer.data)


    if request.method == 'POST':
        serializer = ChatUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            ChatUser.send_email(request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
