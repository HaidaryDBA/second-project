from django.urls import path
from .  import views
from rest_framework.authtoken import views as auth_token
urlpatterns = [
    path("customerList/", views.CustomerShow.as_view(), name="customerList" ),
    path("customerAdd/", views.CustomerAdd.as_view(), name="customerAdd"),
    path("customerUpdate/<int:id>", views.customerUpdate.as_view(), name='customerUpdate'),
    path("customerDelete/<int:id>", views.customerDelete.as_view(), name = "customerDelete"),
    path("employeeAdd/", views.EmployeeAdd.as_view(), name="employeeAdd"),
    path("token/", views.CheckToken.as_view(), name="token"),
    path("login/", auth_token.obtain_auth_token, name="login"),
    path("loggin", views.Authentication.as_view()),
    path("EmployeeList", views.EmployeeList.as_view(), name="EmployeeList"),
    path("EmployeeUpdate/<int:pk>", views.EmployeeUpdate.as_view(), name="EmployeeUpdate"),
    path('EmployeeDelete/<int:id>', views.EmployeeDelete.as_view(), name="EmployeeDelete"),

]
