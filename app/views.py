from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import requests

from app.serializers import UsersSerializer

class UsersView(APIView):
    def get(self, request, format=None):
        main_request = requests.get('https://jsonplaceholder.typicode.com/todos')
        serializer = UsersSerializer(data=main_request.json()[:5], many=True)
        #responses = json.load(main_request.request)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(None)