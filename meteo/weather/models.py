from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        return super(City, self).save(*args, **kwargs)

    def __str__(self): #show the actual city name on the dashboard
        return self.name

    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'