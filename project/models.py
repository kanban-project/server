from django.db import models
from user.models import User
from base.models import ModelBased

class Project(ModelBased):
    id=models.AutoField(primary_key=True)
    title=models.TextField(max_length=50, blank=False)
    description=models.TextField()
    user_id=models.ManyToManyField(User, related_name='user')   #다대다 
#specify table name
    class Meta:
        db_table = 'Kanban_Project'

    def __repr__(self):
        return self.s_name 