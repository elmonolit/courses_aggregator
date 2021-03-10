from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View, CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Course, School, Specialization, CourseReview, SchoolReview
from .forms import SchoolReviewForm, CourseReviewForm, ReviewForm


class Index(ListView):
    model = Course
    template_name = 'index.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schools'] = School.objects.all()
        context['specializations'] = Specialization.objects.all()
        return context


class ModelDetail(DetailView):
    CT = {
        'school': School,
        'specialization': Specialization,
        'course': Course
    }

    context_object_name = 'instance'
    template_name = 'detail.html'
    slug_url_kwarg = 'slug'

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT[kwargs['ct']]
        self.queryset = self.model.objects.all()
        # self.rating_by_review()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if self.model._meta.model_name == 'course':
            form = CourseReviewForm(request.POST)
            inst = form.save(commit=False)
            inst.course_review = self.get_object()
        elif self.model._meta.model_name == 'school':
            form = SchoolReviewForm(request.POST)
            inst = form.save(commit=False)
            inst.school_review = self.get_object()

        if form.is_valid():
            # inst = form.save(commit=False)
            inst.owner = self.request.user.userprofile
            inst.save()
            return redirect(self.get_object())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.model_name
        if context['model_name'] == 'course':
            context['form'] = CourseReviewForm()
        elif context['model_name'] == 'school':
            context['form'] = SchoolReviewForm()
        else:
            context['form'] = None
        return context


class Search(View):
    def result_list_courses(self, startswith, amount=8):
        result = []
        if startswith:
            objects_courses = Course.objects.filter(name__icontains=startswith)[:8]
            objects_schools = School.objects.filter(name__istartswith=startswith)[:8]
            result.extend(objects_courses)
            result.extend(objects_schools)
            return result

    def get(self, request, *args, **kwargs):
        searchbar = request.GET['searchbar']
        result = self.result_list_courses(searchbar)
        return render(request, 'search.html', {'courses': result})


class SignInView(LoginView):
    template_name = 'login.html'


class SignOutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('sign_in')


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'sign_up.html'
    success_url = reverse_lazy('sign_in')
