from django.shortcuts import render
from rest_framework import status
from .models import Articals
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
# Create your views here.


class ArticleListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        article = Articals.objects.all()
        ser = ArticleSerializer(instance = article, many = True)
        return Response(data = ser.data, status = status.HTTP_200_OK)

    # view for adding new article
    def post(self, request):
        user = request.user
        ser = ArticleSerializer(data= request.data)
        if ser.is_valid():
            if request.user.is_authenticated:
                ser.validated_data["user"] = request.user
            ser.save()
            return Response(ser.data, status = status.HTTP_201_CREATED)

        return Response(ser.errors, status = status.HTTP_400_BAD_REQUEST)


class ArticleUpdate(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request,id):
        article = Articals.objects.get(id =id)
        ser = ArticleSerializer(instance = article, data = request.data)
        if ser.is_valid():
            ser.save()
            return Response({"message": "you have updated successfully! "},
                            status= status.HTTP_200_OK)
        return Response(ser.errors, status = status.HTTP_400_BAD_REQUEST)


        


