from django.contrib import admin
from .models import Category, MediaItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name': ('name',)}

@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'title': ('title',)}



