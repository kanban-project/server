from django.urls import path

from .views import UserList, UserDetail, UserViewSet, UserLoginView

urlpatterns = [
    path("", UserList.as_view(), name = UserList.name),
    path("<int:pk>/", UserDetail.as_view(), name = UserDetail.name),
    path("viewset/", UserViewSet.as_view({'get': 'list'}), name = UserViewSet.name),
    path("signup/", UserLoginView.as_view(), name = UserLoginView.name)
]
