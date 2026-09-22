
import re

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView 
from .serializers import UserSerializer
from rest_framework import status
from django.contrib.auth.models import User

# Create your views here.

class UserView(APIView):
    def get(self, request):
        queryset = User.objects.all()
        ser = UserSerializer(instance = queryset, many= True)
        return Response(ser.data)


# Add new User 
class UserAdd(APIView):
    def post(self,request):
        ser = UserSerializer(instance =request.data)
        if ser.is_valid():
            ser.save()
            return Response(instance = ser.data, status = status.HTTP_201_CREATED)
        return Response({"message": "your request is not valid"}, status = status.HTTP_400_BAD_REQUEST)


# Editing the Userview
class UserUpdate(APIView):
    def put(self,request,pk):
        user = User.objects.get(pk=pk)
        ser = UserSerializer(
            instance = user, data = request.data
        )
        if ser.is_valid():
            ser.save()
            return  Response({"message":"you have updated successfully"})

        return Response(status=status.HTTP_400_BAD_REQUEST)