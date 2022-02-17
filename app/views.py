from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import requests
from app.serializers import UsersSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

MAIN_ENDPOINT = "https://jsonplaceholder.typicode.com/todos"


class UsersView(APIView):
    def get(self, request, format=None):
        serializer = UsersSerializer(data=requests.get(MAIN_ENDPOINT).json()[:5], many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
