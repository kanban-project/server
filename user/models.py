from django.db import models
from base.models import ModelBased

class User(ModelBased): #다중상속을 피하기위해
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20) 
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=513) # 512 OR 256  
    autority_choices = (
        (1,'ADMIN'),
        (2,'NORMAL')   )
    autority= models.IntegerField(default=1, choices=autority_choices) #option만들기
  
  #specify table name     
    class Meta:
            db_table = 'Kanban_User'

 