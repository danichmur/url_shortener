from django.contrib import admin
from .models import Shortener

# Register your models here.

# class ShortenerAdmin(admin.ModelAdmin):
# 	pass

admin.site.register(Shortener)