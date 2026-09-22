from rest_framework import serializers
from .models import Articals
from django.contrib.auth.models import User


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articals
        fields = "__all__"
        read_only_fields = ("id","created_at","updated_at")

    def validate_user(self,value):
        existing = User.objects.filter(username = value)
        if not existing :
            raise serializers.ValidationError("این کاربر در سیستم درج نشده است")
        return value

    
