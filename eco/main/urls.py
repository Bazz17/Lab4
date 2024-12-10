from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView, LoginView, TemplateView
from django.urls import path
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # Jedna ruta za login
    path('logout/', LogoutView.as_view(), name='logout'),  # Jedna ruta za logout
    path('logged-out/', TemplateView.as_view(template_name='logged_out.html'), name='logged_out'),  # Stranica nakon odjave
    path('register/', views.register, name='register'),  # Za registraciju
    path('', views.home_view, name='home'),  # Početna stranica
    path('home/', views.home_view, name='home'),  # Još jedna ruta za home
]
