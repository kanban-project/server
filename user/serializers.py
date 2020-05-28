from django.conf.urls import url,include
from .models import User
from rest_framework import serializers
# from django.contrib.auth.models import User, Group

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields =('id','email','name')
