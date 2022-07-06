from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

    
def index(request):
    return render(request, 'index.html')
