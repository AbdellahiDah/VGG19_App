from django.db import models

# Create your models here.
class base_img(models.Model):
    
    photo = models.ImageField(upload_to="photos/")

    def __str__(self):
           return self.nom   