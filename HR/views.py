from django.shortcuts import render
from rest_framework.views import APIView
from .models import Customers,Employee
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from .serializers  import CustomerSerializer,EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated,IsAdminUser,AllowAny
from .permission import CustomerViews,EmployeePermission,GroupePermission
# Create your views here.


class CustomerShow(APIView):
    permission_classes = [CustomerViews]
    def get(self, request):
        customers = Customers.objects.all()
        ser = CustomerSerializer(instance = customers, many = True)
        return Response(ser.data, status=status.HTTP_200_OK)

class CustomerAdd(APIView):
    permission_classes =[GroupePermission]
    def post(self,request):
        ser = CustomerSerializer(data = request.data)
        if ser.is_valid():
            ser.save()
            return Response({"message": " you have addedd successfully a new customer"}, status = status.HTTP_201_CREATED)
        return Response(ser.errors, status = status.HTTP_400_BAD_REQUEST)

class customerUpdate(APIView):
    permission_classes = [GroupePermission]
    def put(self,request, id):
        customer = Customers.objects.get(id = id)
        ser = CustomerSerializer(instance = customer, data = request.data, partial = True)
        if ser.is_valid():
            ser.save()
            return Response("you have updated successfull", status=status.HTTP_200_OK)
        return Response(ser.errors, status = status.HTTP_400_BAD_REQUEST)


class customerDelete(APIView):
    permission_classes = [CustomerViews]
    def delete(self, request, id ):
        customer = Customers.objects.get(id =id)
        customer.delete()
        return Response({"message": f"you have deleted the {id} id customer "})



user = User.objects.all()
# view for Employee
class EmployeeAdd(APIView):
    permission_classes =[EmployeePermission]
    def post(self, request):
        ser = EmployeeSerializer(data = request.data)
        if ser.is_valid():
            ser.save()
            return Response({"message": "you have added a new employee successfully"}, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status= status.HTTP_400_BAD_REQUEST)



# List of Employee
class EmployeeList(APIView):
    permission_classes =[EmployeePermission]
    def get(self, request):
        employee = Employee.objects.all()
        ser = EmployeeSerializer(instance = employee, many= True)
        return Response(data = ser.data, status=status.HTTP_200_OK)


# UPdate Employee
class EmployeeUpdate(APIView):
    permission_classes = [EmployeePermission]
    def put(self, request, pk):
        employee = Employee.objects.get(id = pk)
        ser = EmployeeSerializer(instance = employee ,data = request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status = status.HTTP_200_OK)
        return Response(ser.errors, status = status.HTTP_400_BAD_REQUEST)


        # Delete Employee
class EmployeeDelete(APIView):
    permission_classes = [EmployeePermission]
    def delete(self, request, id):
        employee = Employee.objects.get(id = id)
        employee.delete()
        return Response("you have Deleted successfully",
                        status=status.HTTP_204_NO_CONTENT)

class CheckToken(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]
    def get(self, request):
        user = request.user
        return Response({
            "user": user.username
        })

class Authentication(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(
            request,
            username = username,
            password = password
        )
        if user is None:
            return Response(
                {"Error": "your username or password is Incrrect"},
                status = status.HTTP_401_UNAUTHORIZED
            )

        token, created = Token.objects.get_or_create(user = user)
        return Response({"message": "you have logged in Successfully",
                         "token": token.key},
                         status= status.HTTP_200_OK)
    

