from rest_framework import serializers

from accounts.models import BaseUser, StudentUser, SchoolAdmin

class BaseUserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BaseUser
        fields = ['email','first_name','last_name','password']
        extra_kwargs = {"password" : {"write_only": True}}

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        CustomUser_object = BaseUser(email=email)
        CustomUser_object.set_password(password)
        CustomUser_object.is_superuser = True
        CustomUser_object.save()
        return validated_data



class SchoolAdminCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolAdmin
        fields = ['email','first_name','last_name','password']
        extra_kwargs = {"password" : {"write_only": True}}

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        CustomUser_object = SchoolAdmin(email=email)
        CustomUser_object.set_password(password)
        CustomUser_object.save()
        return validated_data

class UserClass(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ['first_name','last_name','email','is_superuser']

class StudentUserClass(serializers.ModelSerializer):
    class Meta:
        model = StudentUser
        fields = ['first_name','last_name','email','is_superuser','student_id','address','city','state','pincode','phone_number','mother_phone','father_phone','standard']
