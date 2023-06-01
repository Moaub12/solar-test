from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

class LoginView(APIView):
    

    def get(self, request):
        users = User.objects.all()
             
        if users:
            serializer = UserSerializer(users, many=True)
            return Response({'users': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No users found'}, status=status.HTTP_401_UNAUTHORIZED)