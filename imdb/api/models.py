from django.db import models


# Create your models here.






class Movie(models.Model):
    name = models.CharField(max_length=1000,default='No Name Available')
    year = models.IntegerField(default=0000)
    rank = models.IntegerField(default=0000)
    certificate = models.CharField(max_length=10,default='None')
    duration = models.IntegerField(default=0)
    genre = models.CharField(max_length=50,default='None')
    rating = models.DecimalField(decimal_places=1,max_digits=10,default=0.00)
    description = models.CharField(max_length=2000,default='No Description Available')
   

    def __str__(self):
        return self.name
