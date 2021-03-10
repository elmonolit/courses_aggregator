from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('schools', SchoolsViewSet)
router.register('courses', CoursesViewSet)
router.register('specializations', SpecializationViewSet)
router.register('schoolreviews', SchoolReviewViewSet)
router.register('coursereviews', CourseReviewViewSet)
router.register('userprofiles', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
