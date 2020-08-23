from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.IntegerField(default=0)
    img = models.ImageField(upload_to = 'item_pic')
    
    def __str__(self):
        return self.title