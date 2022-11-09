from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger



from .models import *


# Create your views here.

#So I have pagineted (x) amount of items to be displaying on the front end

def home(request):

  #This is a list view of items found
  user_list = User.objects.order_by('id').reverse()    #============      This reverse is used to order IN DESCENDING ORDER
  page = request.GET.get('page', 1)
  paginator = Paginator(user_list, 7)
  try:
    users = paginator.page(page)
  except PageNotAnInteger:
    users = paginator.page(1)
  except EmptyPage:
    users = paginator.page(paginator.num_pages)

  #output  the  data in a simple form
  context = {
    'users':users,
  }
   
  return render(request, 'home.html', context)


def articlelistView(request):

  return render(request, 'article-list.html')


def articleView(request):

  return render( request,'article-page.html')




#Here is the feature to display different types of data

""" 
  # Create your views here.       
def Home(request):
    category = request.GET.get('category')
    if category:
        ls = Item.objects.filter(category=category)
    else:
        ls = Item.objects.all()
    return render(request, 'home.html', {'ls':ls})

 """




