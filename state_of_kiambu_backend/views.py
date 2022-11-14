from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger



from .models import *





# Create your views here.

#So I have pagineted (x) amount of items to be displaying on the front end

def home(request):


  try:
    #The Queries
    newsQ = article.objects.filter(menu="N")
    marketsQ = article.objects.filter(menu="M")
    politicsQ = article.objects.filter(menu="P")
    fictionQ = article.objects.filter(menu="FP")
    booksCultureQ = article.objects.filter(menu="BC")
    humourCartoonsQ = article.objects.filter(menu="HC")
    puzzlesGamesQ = article.objects.filter(menu="PG")
    styleQ = article.objects.order_by('slug').reverse().filter(menu="S")

    

    page = request.GET.get('page', 1)
    paginatorNews = Paginator(newsQ, 4)
    paginatorMarkets = Paginator(marketsQ, 4)
    paginatorPolitics = Paginator(politicsQ, 4)
    paginatorFiction = Paginator(fictionQ, 4)
    paginatorBooksCulture = Paginator(booksCultureQ, 4)
    paginatorHumourCartoons = Paginator(humourCartoonsQ, 4)
    paginatorPuzzleGames = Paginator(puzzlesGamesQ, 4)
    paginatorStyle = Paginator(styleQ, 4)
    try:
      news = paginatorNews.page(page)
      markets = paginatorMarkets.page(page)
      politics = paginatorPolitics.page(page)
      fiction = paginatorFiction.page(page)
      booksCulture = paginatorBooksCulture.page(page)
      humourCartoons = paginatorHumourCartoons.page(page)
      puzzlesGames = paginatorPuzzleGames.page(page)
      style = paginatorStyle.page(page)
      

    except PageNotAnInteger:
      news = paginatorNews.page(1)
      markets = paginatorMarkets.page(1)
      politics = paginatorPolitics.page(1)
      fiction = paginatorFiction.page(1)
      booksCulture = paginatorBooksCulture.page(1)
      humourCartoons = paginatorHumourCartoons.page(1)
      puzzlesGames = paginatorPuzzleGames.page(1)
      style = paginatorStyle.page(1)
      

    except EmptyPage:
      news = paginatorNews.page(paginatorNews.num_pages)
      markets = paginatorMarkets.page(paginatorMarkets.num_pages)
      politics = paginatorPolitics.page(paginatorPolitics.num_pages)
      fiction = paginatorFiction.page(paginatorFiction.num_pages)
      booksCulture = paginatorBooksCulture.page(paginatorBooksCulture.num_pages)
      humourCartoons = paginatorHumourCartoons.page(paginatorHumourCartoons.num_pages)
      puzzlesGames = paginatorPuzzleGames.page(paginatorPuzzleGames.num_pages)
      style = paginatorStyle.page(paginatorStyle.num_pages)

  except:
    print("failed")

  
 

  #output  the  data in a simple form
  context = {
    'news': news,
    'markets': markets,
    'politics': politics,
    'fiction': fiction,
    'booksCulture': booksCulture,
    'humourCartoons': humourCartoons,
    'puzzleGames': puzzlesGames,
    'style': style,   
  }




   
  return render(request, 'home.html', context)




#THis puts all the menu items in a single page
def articlelistView(request, menu):


  TOPICS = request.GET.get('menu')

  # add a sorting algortithm
  topics = article.objects.order_by('slug').reverse().all().values('menu')
  print(topics)
  print(menu)

  if topics:
    artliclelists = article.objects.filter(menu=menu)
    print(artliclelists)
    print("it works")
  else:
    print(' Error Getting the article that matches the menu')


  context = {
    'artliclelists': artliclelists,
  }
  


  return render(request, 'article-list.html', context)






def articleView(request, slug):

  #this line queries the specific article
  articles = article.objects.filter(slug=slug)


  #Reading more recommendation

  #recommendation = article.objects.filter(recommended=0)

  context = {
    'articles': articles,
  }


  return render( request,'article-page.html', context)




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




