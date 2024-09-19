from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import LoginForm, RegisterForm
from .models import User


# def sign_in(request):
#     if request.method == "GET":
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = LoginForm()
#         return render(request, 'users/login.html', {'form': form})
#
#     elif request.method == "POST":
#         form = LoginForm(request.POST)
#
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(request, username=username, password=password)
#
#             if user is not None:
#                 login(request, user)
#                 return redirect('user_profile')
#             else:
#                 messages.error(request, "Invalid username or password.")
#                 return render(request, 'users/login.html', {'form': form})


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('user_profile')
        else:
            return render(request, 'users/register.html', {"form": form})


@login_required
def profile_detail_view(request):
    user_query = User.objects.filter(username=request.user.username)
    return render(request, 'users/profile.html', {'user_profile': user_query})