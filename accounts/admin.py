from django.contrib import admin

# Register your models here.
from .models import Detail, Country, City

admin.site.register(Detail)
admin.site.register(Country)
admin.site.register(City)