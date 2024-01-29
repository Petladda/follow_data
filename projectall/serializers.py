from rest_framework import fields,serializers
from django.contrib.auth import get_user_model
from .models import AppUser

'''class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"'''

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['username','password','id_student' ,'first_name','last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = AppUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.role = "STD"
        user.save()

        return user
        