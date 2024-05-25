from django.db import models

# Create your models here.
class Receipe(models.Model):
    receipe_name=models.CharField(max_length=50)
    receipe_des=models.TextField()    
    receipe_color=models.CharField(max_length=30)
    receipe_image = models.ImageField(upload_to="recipe", default="default_image.jpg")
 