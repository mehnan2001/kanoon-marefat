from django.contrib import admin
from .models import CourseModel, CategoryModel


@admin.register(CourseModel)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
