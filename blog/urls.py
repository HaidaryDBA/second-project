from django.urls import path
from . import views

urlpatterns = [
    path("ArticleList", views.ArticleListView.as_view(), name="ArticleList"),
    path("ArticleUpdate/<int:id>", views.ArticleUpdate.as_view(), name="ArticleUpdate"),
    path("ArticleDelete/<int:id>", views.ArticleDelete.as_view(), name="ArticelDelete"),
]
