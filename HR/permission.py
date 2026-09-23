from rest_framework.permissions import BasePermission

class CustomerViews(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            if request.user.is_staff:
                return True
            self.message ="شما اجازه مشاهده اطلاعات مشتری هارا ندارید"
            return False

        if request.method == "POST":
            if request.user.is_superuser:
                return True
            self.message = "شما نیمتوانید مشتری جدید اضافه کنید"
            return False

        if request.method == "PUT":
            if request.user.is_superuser:
                return True
            self.message="شما نمیتوانید مشخصات کاربر را آپدیت کنید"
            return False
        
        if request.method == "DELETE":
            if request.user.is_superuser:
                return True
            self.message ="شما اجازه حذف کردن این مشتری را ندارید"
            return False
        self.message="شما در این بخش دسترسی ندارید"
        return False

class EmployeePermission(BasePermission):
    def has_permission(self,request,view):
        if request.method == "GET":
            if request.user.is_staff:
                return True
            self.message = "شما دسترسی در بخش کارمندان ندارید"
            return False

        if request.method == "POST":
            if request.user.is_superuser():
                return True
            self.message = "تنها ادمین میتواند کارمند جدید اضافه کند"
            return False
        if request.method == "PUT":
            if request.user.is_superuser:
                return True
            self.message = "تنها ادمین میتواند کاربر را آپدیت کند"
            return False
        if request.method == "DELETE":
            if request.user.is_superuser:
                return True
            self.message = "تنها ادمین میتواند اطلاعات کارمند را حذف کنند"
            return False

        self.message = "ببخشید! شما اجازه دسترسی در این بخش را ندارید"
        return False



class GroupePermission(BasePermission):
    def has_permission(self, request, view):
        admin = request.user.groups.filter(name= "admin").exists()
        return admin
    