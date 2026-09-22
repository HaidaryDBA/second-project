from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length= 200)
    last_name = serializers.CharField(max_length = 50)
    first_name = serializers.CharField(max_length = 50)
    email = serializers.CharField(max_length = 150)