from courses.models import School, Specialization, Course, SchoolReview, CourseReview, UserProfile

from rest_framework.serializers import ModelSerializer


class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        exclude = ('slug',)


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        exclude = ('slug',)


class SpecializationSerializer(ModelSerializer):
    class Meta:
        model = Specialization
        exclude = ('slug',)


class SchoolReviewSerializer(ModelSerializer):
    class Meta:
        model = SchoolReview
        fields = "__all__"


class CourseReviewSerializer(ModelSerializer):
    class Meta:
        model = CourseReview
        fields = "__all__"


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
