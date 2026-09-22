from django.contrib import admin
from .models  import Customers, Employee
# Register your models here.


class CusotmerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name",'father_name',"DOB", 'status']
    search_fields = ["first_name","last_name","father_name","DOB"]
    list_filter = ["status", "DOB"]
 
admin.site.register(Customers,CusotmerAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name",'father_name',"DOB", 'status']
    search_fields = ["first_name","last_name","father_name","DOB"]
    list_filter = ["status", "DOB"]


admin.site.register(Employee,EmployeeAdmin)