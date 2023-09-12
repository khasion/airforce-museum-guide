import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

# Exhibit Model for each Plane/Helicopter
class Exhibit(models.Model):
    exhibit_ID = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    img = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.location + ' | ' + self.name
    
    def get_type(self):
        return self.type
    
    def get_id(self):
        return self.id
    
    def get_img(self):
        return self.img

# Location Description Model
class LocationDescription(models.Model):
    name = models.CharField(max_length=200)
    name_trans = models.CharField(max_length=200)
    text = models.CharField(max_length=100_000)
    lang = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    feat_img = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' | ' + self.text + ' | ' + self.lang
    
    def get_lang(self):
        return self.lang
    
# Exhibit Description Model
class ExhibitDescription(models.Model):
    exhibit = models.ForeignKey(Exhibit, on_delete=models.CASCADE)
    text = models.CharField(max_length=100_000)
    lang = models.CharField(max_length=200)

    def __str__(self):
        return self.exhibit.name + '| ' +  self.text + ' | ' + self.lang

    def get_lang(self):
        return self.lang

    def get_exhibit(self):
        return self.exhibit
