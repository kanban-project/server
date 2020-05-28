from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import User
from .serializers import UserSerializer
#view를 작성하는 대신 viewset클래스에 공통된 기능을 그룹화 시켜 만듦

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    name = "User"
    serializer_class = UserSerializer


class UserList(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'board-list'

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'board-detail'
