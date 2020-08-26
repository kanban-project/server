from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer, UserLoginSerializer
#view를 작성하는 대신 viewset클래스에 공통된 기능을 그룹화 시켜 만듦

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    name = "User"
    serializer_class = UserSerializer


class UserList(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class UserLoginView(generics.RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
    name = 'user-signup'

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token' : serializer.data['token'],
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)