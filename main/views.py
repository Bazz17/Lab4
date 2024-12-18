from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import *

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)


# Provjera da li je korisnik administrator
@login_required
@user_passes_test(lambda u: u.groups.filter(name='Administrator').exists())
def admin_view(request):
    return render(request, 'admin_dashboard.html')
# za običnog smrtnika -> korisnika
@login_required
@user_passes_test(lambda u: u.groups.filter(name='Korisnik').exists())
def user_view(request):
    return render(request, 'user_dashboard.html')

def home_view(request):
    return render(request, 'home.html')


# Base ListView s pretraživanjem
class BaseSearchListView(ListView):
    search_fields = []  # Polja po kojima se pretražuje
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = super().get_queryset()
        if query and self.search_fields:
            q_objects = Q()
            for field in self.search_fields:
                q_objects |= Q(**{f"{field}__icontains": query})
            return queryset.filter(q_objects)
        return queryset

# Habit
class HabitListView(BaseSearchListView):
    model = Habit
    template_name = 'habits/habit_list.html'
    context_object_name = 'habits'
    search_fields = ['name', 'description']

class HabitDetailView(DetailView):
    model = Habit
    template_name = 'habits/habit_detail.html'
    context_object_name = 'habit'

# UserHabit
class UserHabitListView(BaseSearchListView):
    model = UserHabit
    template_name = 'user_habits/user_habit_list.html'
    context_object_name = 'user_habits'
    search_fields = ['user__username', 'habit__name', 'frequency']

class UserHabitDetailView(DetailView):
    model = UserHabit
    template_name = 'user_habits/user_habit_detail.html'
    context_object_name = 'user_habit'

# ActivityLog
class ActivityLogListView(BaseSearchListView):
    model = ActivityLog
    template_name = 'activity_logs/activity_log_list.html'
    context_object_name = 'activity_logs'
    search_fields = ['user_habit__user__username', 'date']

class ActivityLogDetailView(DetailView):
    model = ActivityLog
    template_name = 'activity_logs/activity_log_detail.html'
    context_object_name = 'activity_log'

# Goal
class GoalListView(BaseSearchListView):
    model = Goal
    template_name = 'goals/goal_list.html'
    context_object_name = 'goals'
    search_fields = ['user__username', 'description']

class GoalDetailView(DetailView):
    model = Goal
    template_name = 'goals/goal_detail.html'
    context_object_name = 'goal'

# Badge
class BadgeListView(BaseSearchListView):
    model = Badge
    template_name = 'badges/badge_list.html'
    context_object_name = 'badges'
    search_fields = ['name', 'description', 'criteria']

class BadgeDetailView(DetailView):
    model = Badge
    template_name = 'badges/badge_detail.html'
    context_object_name = 'badge'

# UserBadge
class UserBadgeListView(BaseSearchListView):
    model = UserBadge
    template_name = 'user_badges/user_badge_list.html'
    context_object_name = 'user_badges'
    search_fields = ['user__username', 'badge__name']

class UserBadgeDetailView(DetailView):
    model = UserBadge
    template_name = 'user_badges/user_badge_detail.html'
    context_object_name = 'user_badge'

# Tip
class TipListView(BaseSearchListView):
    model = Tip
    template_name = 'tips/tip_list.html'
    context_object_name = 'tips'
    search_fields = ['title', 'content']

class TipDetailView(DetailView):
    model = Tip
    template_name = 'tips/tip_detail.html'
    context_object_name = 'tip'
