from django.db import models

# Create your models here.
class Customers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    phone = models.CharField(unique= True,max_length=12 )
    Email = models.EmailField(unique=True, null=True, blank=True)
    address = models.CharField(max_length=255)
    DOB = models.DateField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add =False, auto_now =True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        unique_together = ["first_name","last_name","father_name"]


# Employee Model
class Employee(models.Model):
        genderList = [
             ('male',"Male"),
             ('famale','Famale')
            
        ]
         
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        father_name = models.CharField(max_length=100)
        phone = models.CharField(unique= True,max_length=12 )
        gender = models.CharField(max_length=100, choices=genderList, default="male")
        Email = models.EmailField(unique=True, null=True, blank=True)
        address = models.CharField(max_length=255)
        DOB = models.DateField()
        status = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
        updated_at = models.DateTimeField(auto_now_add =False, auto_now =True)

        def __str__(self):
            return f"{self.first_name} {self.last_name}"

        class Meta:
             unique_together = ("first_name", "last_name", 'father_name')