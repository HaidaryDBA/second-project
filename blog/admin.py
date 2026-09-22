from django.contrib import admin
from .models import Articals
# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    list_display  = ["user", "title", "created_at"]
    search_fields = ["user","title"]
    list_filter = ("user",)
admin.site.register(Articals,ArticlesAdmin)