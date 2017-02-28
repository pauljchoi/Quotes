from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')

def register(request):
    response = User.objects.add_user(request.POST)
    if response['status']:
        request.session['user_id'] = response['user'].id
        request.session['user_name'] = response['user'].name
        request.session['user_alias'] = response['user'].alias
        return redirect('quotes:index')
    else:
        for error in response['errors']:
            messages.error(request, error)
    return redirect('users:index')

def login(request):
    response = User.objects.check_user(request.POST)
    if response['status']:
        request.session['user_id'] = response['loggedin_user'].id
        request.session['user_name'] = response['loggedin_user'].name
        request.session['user_alias'] = response['loggedin_user'].alias
        return redirect('quotes:index')
    else:
        for error in response['errors']:
            messages.error(request, error)
    return redirect('users:index')

def success(request):
    return render(request, 'main_app/success.html')

def logout(request):
    request.session.clear()
    return redirect('users:index')
