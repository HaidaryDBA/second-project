from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Articals(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True, blank = True)
    title = models.CharField(max_length=255,null=False, blank=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now = False)
    updated_at = models.DateTimeField(auto_now= True, auto_now_add=False)


    def __str__(self):
        return f"{self.user} - {self.title}"
    
