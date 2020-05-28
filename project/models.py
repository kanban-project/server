from django.db import models


class ModelBased(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True


class Project(ModelBased):
    id=models.AutoField(primary_key=True)
    title=models.TextField(max_length=50, blank=False)
    description=models.TextField()

class Meta:
         ordering = ['-dute_date'] #내림차순


def __repr__(self):
    return self.s_name 