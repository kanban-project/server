from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer


class TaskList(generics.ListCreateAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    name = 'Task-list'


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    name = 'Task-detail'

class Project_TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    name = 'Project_TaskList'
    def get_queryset(self):
        return Task.objects.filter(project_id=self.kwargs['project'])
        # ,status=self.kwargs['status'])
        
class Project_Task_Status(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    name= 'Project_Task_Status'
    def get_queryset(self):
        return Task.objects.filter(project_id=self.kwargs['project']).filter(status=self.kwargs['status'])




