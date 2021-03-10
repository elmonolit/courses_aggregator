# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import SchoolReview
from .models import CourseReview


class SchoolReviewForm(forms.ModelForm):
    class Meta:
        model = SchoolReview
        fields = ('rating', 'comment',)


class CourseReviewForm(forms.ModelForm):
    class Meta:
        model = CourseReview
        fields = ('rating', 'comment',)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = None
        fields = ('rating', 'comment',)
