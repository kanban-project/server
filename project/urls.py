from django.urls import path

from .views import ProjectList, ProjectDetail

urlpatterns = [
    path("", ProjectList.as_view(), name = ProjectList.name),
    path("<int:pk>/", ProjectDetail.as_view(), name = ProjectDetail.name)
]
