from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.models import CustomUser
from users.api.serializers import CustomUserSerializer

class CustomUserList(APIView):
    """
    List all users for admin. Should always require authentication
    """
    def get(self, request, format=None):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)