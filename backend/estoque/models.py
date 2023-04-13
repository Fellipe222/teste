from django.db import models

# Create your models here.
class Material(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    
