from rest_framework import serializers


class UsersSerializer(serializers.Serializer):
    userId = serializers.IntegerField()
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    completed = serializers.BooleanField()