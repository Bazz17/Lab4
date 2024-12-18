from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView, LoginView, TemplateView
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # Jedna ruta za login
    path('logout/', LogoutView.as_view(), name='logout'),  # Jedna ruta za logout
    path('logged-out/', TemplateView.as_view(template_name='logged_out.html'), name='logged_out'),  # Stranica nakon odjave
    path('register/', views.register, name='register'),  # Za registraciju
    path('', views.home_view, name='home'),  # Početna stranica
    path('home/', views.home_view, name='home'),  # Još jedna ruta za home
    # Habit
    path('habits/', HabitListView.as_view(), name='habit-list'),
    path('habits/<int:pk>/', HabitDetailView.as_view(), name='habit-detail'),
    
    # UserHabit
    path('user-habits/', UserHabitListView.as_view(), name='userhabit-list'),
    path('user-habits/<int:pk>/', UserHabitDetailView.as_view(), name='userhabit-detail'),
    
    # ActivityLog
    path('activity-logs/', ActivityLogListView.as_view(), name='activitylog-list'),
    path('activity-logs/<int:pk>/', ActivityLogDetailView.as_view(), name='activitylog-detail'),
    
    # Goal
    path('goals/', GoalListView.as_view(), name='goal-list'),
    path('goals/<int:pk>/', GoalDetailView.as_view(), name='goal-detail'),
    
    # Badge
    path('badges/', BadgeListView.as_view(), name='badge-list'),
    path('badges/<int:pk>/', BadgeDetailView.as_view(), name='badge-detail'),
    
    # UserBadge
    path('user-badges/', UserBadgeListView.as_view(), name='userbadge-list'),
    path('user-badges/<int:pk>/', UserBadgeDetailView.as_view(), name='userbadge-detail'),
    
    # Tip
    path('tips/', TipListView.as_view(), name='tip-list'),
    path('tips/<int:pk>/', TipDetailView.as_view(), name='tip-detail'),
]