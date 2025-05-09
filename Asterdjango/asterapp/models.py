from django.db import models

# Create your models here.
class Director(models.Model):
    name=models.CharField(max_length=300)
    def __str__(self):
        return self.name

class Censorinfo(models.Model):
    rating=models.CharField(max_length=10,null=True)
    cirtified_by=models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.cirtified_by




class Moviesinfo(models.Model):
    title=models.CharField(max_length=200)
    year=models.IntegerField(null=True)
    description=models.TextField()
    poster=models.ImageField(upload_to='images/',null=True)
    censor_details=models.OneToOneField(Censorinfo,on_delete=models.SET_NULL,related_name="movie",null=True)
    directed_by=models.ForeignKey(Director,null=True,
                                  on_delete=models.CASCADE,
                                  related_name='directed_movies')



    def __str__(self):
        return self.title


