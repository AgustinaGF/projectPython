from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

    
def index(request):
    print(request.user)
    print (request.user.is_authenticated)
    print(request.user.pk)
    return render(request, 'index.html')
