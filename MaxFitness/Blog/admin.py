from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'post_date')

@admin.register(models.Bloggers)
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('blogger_id', 'first_name', 'last_name', 'email')
