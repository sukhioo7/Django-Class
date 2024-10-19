from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'post_date')
