from django.urls import path

from django.contrib.auth.views import LogoutView, LoginView

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<str:ct>/<slug:slug>/', views.ModelDetail.as_view(), name='detail'),
    path('search/', views.Search.as_view(), name='search'),
    path('login/', views.SignInView.as_view(), name='sign_in'),
    path('logout/', views.SignOutView.as_view(), name='sign_out'),
    path('sign_up/', views.SignUp.as_view(), name='sign_up'),

]
