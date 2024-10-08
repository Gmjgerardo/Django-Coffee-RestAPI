from django.contrib import admin
from .models import Coffee, Size, Type

admin.site.register([Size, Type, Coffee])
