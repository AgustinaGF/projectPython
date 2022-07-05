from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from users.models import User_profile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from users.forms import User_registration_form
from django.views.generic import ListView, DetailView,CreateView, DeleteView, UpdateView


def login_view(request):
    if request.method == 'POST':
        form= AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username)
            print(password)
            user = authenticate(username=username, password=password)
            print(user)

            if user is not None:
                login(request, user)
                context = {'message':f'Welcome {username}!!'}
                return render(request, "index.html", context=context)
            else:
                context = {'error':'There is no user with those credentials'}
                form = AuthenticationForm()
                return render(request, 'auth/login.html', context=context)

        else:     
            errors = form.errors   
            form = AuthenticationForm()
            context ={'errors':errors, 'form':form}
            return render(request, 'auth/login.html', context = context)    
    
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render (request,'auth/login.html' ,context=context)

def register_view(request):
    if request.method == 'POST':
        form= User_registration_form(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username= username, password=password)
            login(request, user)
            context = {'message':f'User created successfully, Welcome{username}'}
            return render(request, 'index.html', context = context)
        else:
            errors= form.errors
            form = User_registration_form()
            context = {'errors': errors, 'form': form}
            return render(request, 'auth/register.html', context=context)
    else:
        form = User_registration_form()
        context = {'form': form}
        return render (request, 'auth/register.html', context = context )

def logout_view(request):
    logout(request)
    return redirect('index')


class User_info(LoginRequiredMixin,DetailView):
    model = User_profile
    template_name = 'auth/user.html'

class Update_user(LoginRequiredMixin,UpdateView):
    model = User_profile
    template_name = 'auth/user_update.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('user', kwargs={'pk':self.object.pk})