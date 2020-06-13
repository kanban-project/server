from django.db import models

# Create your models here.
class ModelBased(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, #auto_now_add->date.today() 최초저장
                                      editable=False,
                                      null=False,
                                      blank=True)
    updated_At = models.DateTimeField(auto_now=True,
                                      editable=False, 
                                      null=False, 
                                      blank=False) #auto_now->date.today() save저장될 때 마다
    class Meta:
        abstract = True
        