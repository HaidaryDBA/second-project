from rest_framework import serializers
from .models import Customers,Employee
from datetime import date
from rest_framework.validators import UniqueTogetherValidator,UniqueForDateValidator, UniqueForMonthValidator,UniqueValidator

class CustomerSerializer(serializers.ModelSerializer):
    # status = serializers.BooleanField(write_only = True)
    class Meta:
        model = Customers
        fields = "__all__"
        read_only_fields = ["create_at", "updated_at", "id"]

# phone validation attributes
    def validate_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError(
                "شماره تلفن نمیتواند غیر از اعداد باشد"
            )
        if len(value) != 10:
            raise serializers.ValidationError(
                "شماره تلفن داخلی افغانستان باید دقیفا ۱۰ رقم باشد"
            )
        if not value.startswith("07"):
            raise serializers.ValidationError(
                "شماره تلفن باید با ۰۷ شروع شود"
            )

        existing = Customers.objects.filter(phone = value)

        if self.instance is not None:
            existing = existing.exclude(pk = self.instance.customer_id)

        if existing.exists():
            raise serializers.ValidationError(
                "این شماره تلفن قبلا ‌ذخیره شده است."
            )
        return value

    def validate_DOB(self, value):
        if value >= date.today():
            raise serializers.ValidationError(
                "لطفا تاریخ تولد را قبل از امروز انتخاب نمایید!"
            )
        return value
        



# Validation attributes with Function
def check_phone(value):
    if len(value) != 10:
        raise serializers.ValidationError(
            "شماره تلفن شما باید دقیقا ۱۰ رقم باشد"
        )


# serializer for Employee modelView

class EmployeeSerializer(serializers.ModelSerializer):

    phone = serializers.CharField(
        max_length=10,
        validators=[check_phone]
    )

    class Meta:
        def check_phone(value):
            if len(value["phone"]) != 10:
                raise serializers.ValidationError(
                    "شماره تلفن باید ۱۰ رقم باشد"
                ) 
        def check_date_of_birth(value):
            if value["DOB"] >= date.today():
                raise serializers.ValidationError(
                    "تاریخ تولد را قبل از امروز تعیین کنید"
                )
                
        
        model = Employee
        fields = [
            'id',
            'first_name',
            'last_name',
            'father_name',
            'DOB',
            'phone',
            'gender',
            'address',
            'Email',
            'status',
        ]
        validators = [check_phone, check_date_of_birth]
        


