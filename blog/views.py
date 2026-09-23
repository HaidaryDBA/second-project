from django.shortcuts import render
from rest_framework import status
from .models import Articals
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .permission import IsUserOrReadOnly
# Create your views here.


class ArticleListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        article = Articals.objects.all()
        ser = ArticleSerializer(instance = article, many = True)
        return Response(data = ser.data, status = status.HTTP_200_OK)

    # view for adding new article
    def post(self, request):
        self.permission_classes = [IsAuthenticated, IsUserOrReadOnly]
        
        ser = ArticleSerializer(data= request.data)
        if ser.is_valid():
            if request.user.is_authenticated:
                ser.validated_data["user"] = request.user
            ser.save()
            return Response(ser.data, status = status.HTTP_201_CREATED)

        return Response(ser.errors, status = status.HTTP_400_BAD_REQUEST)


class ArticleUpdate(APIView):
    permission_classes = [IsAuthenticated, IsUserOrReadOnly]
    
    def put(self, request,id):
        article = Articals.objects.get(id =id)
        self.check_object_permissions(request, article)
        ser = ArticleSerializer(instance = article, data = request.data)
        if ser.is_valid():
            ser.save()
            return Response({"message": "you have updated successfully! "},
                            status= status.HTTP_200_OK)
        return Response(ser.errors, status = status.HTTP_400_BAD_REQUEST)


class ArticleDelete(APIView):
    permission_classes = [IsAuthenticated, IsUserOrReadOnly]
    def delete(self, request, id ):
        article = Articals.objects.get(id = id)
        self.check_object_permissions()
        art = article
        article.delete()
        return Response({"message": f" you have deleted  the Article {art}" },
                        status= status.HTTP_204_NO_CONTENT)


