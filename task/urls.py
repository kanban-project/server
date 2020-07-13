from django.urls import path

from .views import TaskList, TaskDetail, Project_TaskList

urlpatterns = [
    path("", TaskList.as_view(), name = TaskList.name), #/post/
    path("<int:pk>/", TaskDetail.as_view(), name = TaskDetail.name), #/get(pk번포스팅)/put(pk번수정)/delete(pk번삭제)
    path("project/<int:project>", Project_TaskList.as_view(), name=Project_TaskList.name)
]



