from tabnanny import verbose
from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self): # show the actual city name on the dashboard
        return self.name

    class Meta: # To show plural of the city as cities instead of citys
        verbose_name_plural = 'cities'