from django.db import models

# Create your models here.
class Document(models.Model):
    name=models.CharField(max_length=100) 
    glb_file=models.FileField(upload_to="./glbs/")
    def __str__(self):
        return self.name