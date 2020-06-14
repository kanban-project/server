from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer


class TaskList(generics.ListCreateAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    name = 'Task-list'

def get_query(self):
    
    return Task.objects.filter(project_id=self.kwargs['project'])

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    name = 'Task-detail'





