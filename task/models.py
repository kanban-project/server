from django.db import models
from user.models import User
from project.models import Project


class ModelBased(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True


class Task(ModelBased):
    id=models.AutoField(primary_key=True)
    user_id=models.ManyToManyField(User, related_name='user')   #다대다 
    project_id=models.ForeignKey(Project, 
                                 on_delete=models.CASCADE,
                                 related_name='project')#다대일
    title=models.TextField(max_length=200, blank=False)
    description=models.TextField() #long text
    due_date=models.DateTimeField()
    """
    class status(models.IntegerChoices):
            Open = 1
            InProgress = 2
            Completed = 3
            closed = 4
    """
    status=models.IntegerField(default=1)
    
    def __repr__(self): #개발자끼리의 공유(보여주기용) <-> str
            return self.user_id +':' +self.title #task tile과 name이 뜸