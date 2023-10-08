from django.db import models

# Create your models here.
class Books(models.Model):
    name=models.CharField(max_length=50)
    des=models.TextField()
    image=models.ImageField(upload_to="bk_pics",max_length=500)
    price=models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    