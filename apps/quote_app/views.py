from django.shortcuts import render, redirect
from ..main_app.models import User

from .models import Quote, Favorite
# Create your views here.
def index(request):
    context = {
        'contents': Quote.objects.all(),
        'user': User.objects.get(id=request.session['user_id']),
        'favorites': Favorite.objects.filter(user = User.objects.get(id=request.session['user_id']))
    }

    return render(request, 'quote_app/index.html', context)

def create(request):
    user = User.objects.get(id=request.session['user_id'])
    content = Quote.objects.create(content=request.POST['content'], user = user)

    return redirect('quotes:index')

def favorite_add(request, quote_id):
    user = User.objects.get(id=request.session['user_id'])
    quote = Quote.objects.get(id=quote_id)
    Favorite.objects.create(quote = quote, user = user)
    return redirect('quotes:index')

def show_user(request, user_id):
    user = User.objects.get(id=user_id)
    context ={
           'contents': Quote.objects.filter(user = user),
           'user': user,
           }
    return render(request, 'quote_app/show.html', context)

def delete_quote(request, quote_id):
    this = Favorite.objects.get(quote = Quote.objects.get(id=quote_id))
    this.delete()
    # this.save()
    return redirect('quotes:index')
