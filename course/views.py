from rest_framework import generics, mixins, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course, Review
from .serializers import CourseSerializers, ReviewSerializers

# ==================================== API V1 ====================================
class CoursesAPIView(generics.ListCreateAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializers
class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializers
  
class ReviewsAPIView(generics.ListCreateAPIView):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializers

  def get_queryset(self):
    course_pk = self.kwargs.get('course_pk')
    if course_pk:
      return self.queryset.filter(course_id=course_pk)
    return self.queryset.all()
  
class ReviewAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializers

  def get_object(self):
    course_pk = self.kwargs.get('course_pk')
    review_pk = self.kwargs.get('review_pk')

    if course_pk:
      return get_object_or_404(self.get_queryset(), course_id=course_pk, pk=review_pk)
    return get_object_or_404(self.get_queryset(), pk=review_pk)

# ==================================== API V2 ====================================

class CourseViewSet(viewsets.ModelViewSet):
  queryset = Course.objects.all()
  serializer_class = CourseSerializers

  @action(detail=True, methods=['get'])
  def reviews(self, request, pk=None):
    course = self.get_object()
    serializer = ReviewSerializers(course.reviews.all(), many=True)
    return Response(serializer.data)
  
#   ViewSet Padrão
# class ReviewViewSet(viewsets.ModelViewSet):
#   queryset = Review.objects.all()
#   serializer_class = ReviewSerializers

class ReviewViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializers