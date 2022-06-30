from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

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


def index(request):
    print(request.user)
    print (request.user.is_authenticated)
    return render(request, 'index.html')
