from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django_base.forms import User_registration_form


    
def index(request):
    print(request.user)
    print (request.user.is_authenticated)
    return render(request, 'index.html')
