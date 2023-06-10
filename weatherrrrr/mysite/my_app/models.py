from django.db import models

from django.db import models
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.

def validate_even(value):
    if (value > 127) and (value<0):
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )
    
class Continent(models.Model):
    continent_name = models.CharField(max_length=50, unique=True, null=True)
    def __str__(self):
        return self.continent_name
    
class Country(models.Model):

    continent = models.ForeignKey(
        Continent, on_delete=models.CASCADE, related_name="country")
    country_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.country_name
    
class City(models.Model):
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="city")
    city_name = models.CharField(max_length=255)

    def __str__(self):
        return self.city_name
    
class Date(models.Model):
    date = models.DateField(unique=True)

    def __datetime__(self):
        return self.date
    
class Time(models.Model):
    time = models.TimeField(unique=True)

    def __datetime__(self):
        return self.time
    
    
class Sky(models.Model):
    sky = models.ImageField(upload_to='media/')

    def __ImageFieldFile__(self):
        return self.sky
    
    
    
class Temp(models.Model):
    temp = models.IntegerField()

    def __str__(self):
        return self.temp

    
class TimeWeather(models.Model):
    
    time = models.TimeField()
    temp = models.IntegerField()
    sky = models.ImageField(upload_to='media/')

class TimeWeather6(models.Model):
    
    time = models.TimeField()
    temp = models.IntegerField()
    sky = models.ImageField(upload_to='media/')

class TimeWeather9(models.Model):
    
    time = models.TimeField()
    temp = models.IntegerField()
    sky = models.ImageField(upload_to='media/')

class TimeWeather12(models.Model):
    
    time = models.TimeField()
    temp = models.IntegerField()
    sky = models.ImageField(upload_to='media/')

class TimeWeather15(models.Model):
    
    time = models.TimeField()
    temp = models.IntegerField()
    sky = models.ImageField(upload_to='media/')

class TimeWeather20(models.Model):
    
    time = models.TimeField()
    temp = models.IntegerField()
    sky = models.ImageField(upload_to='media/')

class TimeWeather23(models.Model):
    
    time = models.TimeField()
    temp = models.IntegerField()
    sky = models.ImageField(upload_to='media/')

    
class TimeRise(models.Model):
    timeRise = models.TimeField()

    def __datatime__(self):
        return self.timeRise
    
class TimeSet(models.Model):
    timeSet = models.TimeField()

    def __datatime__(self):
        return self.timeSet
    
class Attent(models.Model):
    atttent_name = models.CharField(max_length=500)

    def __str__(self):
        return self.atttent_name
    


class DateWeather(models.Model):

    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="dateweather")
    
    date = models.DateField(unique=True)
    
    timeWeather = models.ForeignKey(
        TimeWeather, on_delete=models.CASCADE, related_name="timeweather", null=True)
    
    timeWeather6 = models.ForeignKey(
        TimeWeather6, on_delete=models.CASCADE, related_name="timeweather6", null=True)
    
    timeWeather9 = models.ForeignKey(
        TimeWeather9, on_delete=models.CASCADE, related_name="timeweather9", null=True)
    
    timeWeather12 = models.ForeignKey(
        TimeWeather12, on_delete=models.CASCADE, related_name="timeweather12", null=True)
   
    timeWeather15 = models.ForeignKey(
        TimeWeather15, on_delete=models.CASCADE, related_name="timeweather15", null=True)
    
    timeWeather20 = models.ForeignKey(
        TimeWeather20, on_delete=models.CASCADE, related_name="timeweather20", null=True)
    
    timeWeather23 = models.ForeignKey(
        TimeWeather23, on_delete=models.CASCADE, related_name="timeweather23", null=True)
    
    timeRise = models.TimeField()
    timeSet = models.TimeField()
    
    atttent_name = models.CharField(max_length=500)
