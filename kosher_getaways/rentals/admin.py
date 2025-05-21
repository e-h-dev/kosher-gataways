from django.contrib import admin
from .models import Location, Rentals

# Register your models here.

admin.site.register(Rentals)
admin.site.register(Location)
