from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import authenticate, login

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