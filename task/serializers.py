from .models import Task
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Task
        fields =('id','user_id','project_id','title','description','due_date','status')