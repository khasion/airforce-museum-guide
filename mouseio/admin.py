from django.contrib import admin

# Register your models here.
from .models import Exhibit, LocationDescription, ExhibitDescription

admin.site.register(Exhibit)
admin.site.register(LocationDescription)
admin.site.register(ExhibitDescription)