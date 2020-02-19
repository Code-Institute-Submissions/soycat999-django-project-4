from django.contrib import admin

# Register your models here.
from .models import Games, Category

admin.site.register(Games)
admin.site.register(Category)