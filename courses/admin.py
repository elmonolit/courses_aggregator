from django.contrib import admin

from .models import School, Course, Specialization

admin.site.register(Specialization)
admin.site.register(School)
admin.site.register(Course)
