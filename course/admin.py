from django.contrib import admin
from .models import Course, Review

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
  list_display = ('title', 'url', 'created_at', 'updated_at', 'activated')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
  list_display = ('course', 'name', 'email', 'review', 'created_at', 'updated_at', 'activated')