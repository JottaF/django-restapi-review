from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Review
from .serializers import CourseSerializers, ReviewSerializers

class CourseAPIView(APIView):

  def get(self, request):
    courses = Course.objects.all()
    serializer = CourseSerializers(courses, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = CourseSerializers(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status.HTTP_201_CREATED)
  

class ReviewAPIView(APIView):

  def get(self, reuquest):
    reviews = Review.objects.all()
    serializer = ReviewSerializers(reviews, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = ReviewSerializers(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status.HTTP_201_CREATED)

