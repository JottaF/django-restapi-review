from rest_framework import serializers
from .models import Course, Review

class ReviewSerializers(serializers.ModelSerializer):
  class Meta:
    extra_kwargs = {
      'email': {'write_only': True}
    }
    model = Review
    fields = (
      'id',
      'course',
      'name',
      'email',
      'review',
      'created_at',
      'activated'
    )

class CourseSerializers(serializers.ModelSerializer):
  class Meta:
    model = Course
    fields = (
      'id',
      'title',
      'url',
      'created_at',
      'activated'
    )