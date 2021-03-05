from django.contrib import admin

from .models import School, Course, Specialization, SchoolReview, CourseReview,UserProfile

admin.site.register(Specialization)
admin.site.register(School)
admin.site.register(Course)
admin.site.register(SchoolReview)
admin.site.register(CourseReview)
admin.site.register(UserProfile)
