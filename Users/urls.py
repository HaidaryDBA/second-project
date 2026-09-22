from django.urls import path
from . import views 

urlpatterns = [
    path("users/",views.UserView.as_view(), name="users"),
    path("users/update/<int:pk>",views.UserUpdate.as_view(), name="updateUser"),
    path("AddUser", views.UserAdd.as_view(), name="AddUser"),
]
