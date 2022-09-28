from django.contrib import admin

# Register your models here.
from .models import Directors, Movies
admin.site.register(Directors)
admin.site.register(Movies)
