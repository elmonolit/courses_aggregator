from rest_framework.viewsets import ModelViewSet, ViewSet

from .serializers import *

# class BaseViewSet(ViewSet):
#     def get

class SchoolsViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class CoursesViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class SpecializationViewSet(ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class SchoolReviewViewSet(ModelViewSet):
    queryset = SchoolReview.objects.all()
    serializer_class = SchoolReviewSerializer


class CourseReviewViewSet(ModelViewSet):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewSerializer


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
