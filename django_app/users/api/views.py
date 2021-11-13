from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.api.serializers import CustomUserSerializer
from users.models import CustomUser


class CustomUserList(APIView):
    """
    List all users for admin. Should always require authentication
    """

    def get(self, request, format=None):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)


class CustomUserDetail(APIView):
    """
    Detail of one user. Should always require authentication
    """

    def get_object(self, uuid):
        try:
            return CustomUser.objects.get(uuid=uuid)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, uuid, format=None):
        user = self.get_object(uuid)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
