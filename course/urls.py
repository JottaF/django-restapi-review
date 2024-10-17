from django.urls import path
from .views import CourseAPIView, CoursesAPIView, CourseViewSet, ReviewAPIView, ReviewsAPIView, ReviewViewSet
from rest_framework.routers import SimpleRouter

# ============= API v1 ===============
urlpatterns = [
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('courses/<int:course_pk>/', CourseAPIView.as_view(), name='course'),

    path('courses/<int:course_pk>/reviews/', ReviewsAPIView.as_view(), name='course_reviews'),
    path('courses/<int:course_pk>/reviews/<int:review_pk>', ReviewAPIView.as_view(), name='course_review'),

    path('reviews/<int:pk>/', ReviewAPIView.as_view(), name='review'),
    path('reviews/', ReviewsAPIView.as_view(), name='reviews'),
]


# ============= API v2 ===============
router = SimpleRouter()
router.register('courses', CourseViewSet)
router.register('reviews', ReviewViewSet)