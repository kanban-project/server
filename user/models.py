from django.db import models

class ModelBased(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True


class User(ModelBased): #다중상속을 피하기위해
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20) 
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=513) # 512 OR 256
    """
    class Autority(models.IntegerChoices):
        NORMAL=2
        ADMIN=1
    """
    autority= models.IntegerField(default=1) #option만들기  