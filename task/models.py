from django.db import models
from user.models import User
from project.models import Project
from base.models import ModelBased




class Task(ModelBased):
    id=models.AutoField(primary_key=True)
#     author=models.ManyToManyField(User, related_name='author')   #다대다 
    project_id=models.ForeignKey(Project, 
                                 on_delete=models.CASCADE,
                                 related_name='project')#다대일
    title=models.TextField(max_length=200, blank=False)
    description=models.TextField() #long text
    due_date=models.DateField(null=True)
    status_choices = (
            (1,'Open'),
            (2,'InProgress'),   
            (3,'Completed'),
            (4,'closed')
    )
    status=models.SmallIntegerField(default=1, choices=status_choices)
    priority_choices = (
            (1,'high'),
            (2,'middle'),
            (3, 'low')
    )
    priority=models.SmallIntegerField(default='middle', choices=priority_choices)

#specify table name     
    class Meta:
            db_table = 'Kanban_Task'
            
    def __repr__(self): #개발자끼리의 공유(보여주기용) <-> str
            return self.user_id +':' +self.title #task tile과 name이 뜸            