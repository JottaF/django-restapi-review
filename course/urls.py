from django.urls import path
from .views import CourseAPIView, CoursesAPIView, ReviewAPIView, ReviewsAPIView

urlpatterns = [
    path('courses/<int:pk>', CourseAPIView.as_view(), name='course'),
    path('courses/', CoursesAPIView.as_view(), name='courses'),

    path('reviews/<int:pk>', ReviewAPIView.as_view(), name='review'),
    path('reviews/', ReviewsAPIView.as_view(), name='reviews'),
]
