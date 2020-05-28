from django.urls import path

from .views import TaskList, TaskDetail

urlpatterns = [
    path("", TaskList.as_view(), name = TaskList.name),
    path("<int:pk>/", TaskDetail.as_view(), name = TaskDetail.name)
]
