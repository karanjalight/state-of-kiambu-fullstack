from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger





from .models import *

#User authentication

from .forms import CreateUserForm

from django.contrib.auth.decorators import login_required



def Signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = CreateUserForm()
    return render(request, 'Register.html', {'form': form})







# Create your views here.



#So I have pagineted (x) amount of items to be displaying on the front end

def home(request):


  try:
    #The Queries
    allQ = article.objects.all()
    newsQ = article.objects.filter(menu="News")
    marketsQ = article.objects.filter(menu="Markets")
    politicsQ = article.objects.filter(menu="Politics")
    fictionQ = article.objects.filter(menu="Fiction-and-Poetry")
    booksCultureQ = article.objects.filter(menu="Books-and-Culture")
    humourCartoonsQ = article.objects.filter(menu="Humour-and-Cartoons")
    puzzlesGamesQ = article.objects.filter(menu="Puzzles-and-Games")
    styleQ = article.objects.order_by('slug').reverse().filter(menu="Style")

    

    page = request.GET.get('page', 1)
    paginatorall = Paginator(allQ, 3)
    paginatorNews = Paginator(newsQ, 4)
    paginatorMarkets = Paginator(marketsQ, 4)
    paginatorPolitics = Paginator(politicsQ, 4)
    paginatorFiction = Paginator(fictionQ, 4)
    paginatorBooksCulture = Paginator(booksCultureQ, 4)
    paginatorHumourCartoons = Paginator(humourCartoonsQ, 4)
    paginatorPuzzleGames = Paginator(puzzlesGamesQ, 4)
    paginatorStyle = Paginator(styleQ, 4)
    try:
      all = paginatorall.page(page)
      news = paginatorNews.page(page)
      markets = paginatorMarkets.page(page)
      politics = paginatorPolitics.page(page)
      fiction = paginatorFiction.page(page)
      booksCulture = paginatorBooksCulture.page(page)
      humourCartoons = paginatorHumourCartoons.page(page)
      puzzlesGames = paginatorPuzzleGames.page(page)
      style = paginatorStyle.page(page)
      

    except PageNotAnInteger:
      all = paginatorall.page(1)
      news = paginatorNews.page(1)
      markets = paginatorMarkets.page(1)
      politics = paginatorPolitics.page(1)
      fiction = paginatorFiction.page(1)
      booksCulture = paginatorBooksCulture.page(1)
      humourCartoons = paginatorHumourCartoons.page(1)
      puzzlesGames = paginatorPuzzleGames.page(1)
      style = paginatorStyle.page(1)
      

    except EmptyPage:
      all1 = paginatorall.page(paginatorNews.num_pages)
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


#==========THE LIST VIEWS==================
  
  try:
    #The Queries
    allQL = article.objects.all()
    newsQL = article.objects.filter(menu="News")
    marketsQL = article.objects.filter(menu="Markets")
    politicsQL = article.objects.filter(menu="Politics")
    fictionQL = article.objects.filter(menu="Fiction-and-Poetry")
    booksCultureQL = article.objects.filter(menu="Books-and-Culture")
    humourCartoonsQL = article.objects.filter(menu="Humour-and-Cartoons")
    puzzlesGamesQL = article.objects.filter(menu="Puzzles-and-Games")
    styleQL = article.objects.order_by('slug').reverse().filter(menu="Style")

    

    page = request.GET.get('page', 1)
    paginatorall1 = Paginator(allQL, 3)
    paginatorNews1 = Paginator(newsQL, 1)
    paginatorMarkets1 = Paginator(marketsQL, 1)
    paginatorPolitics1 = Paginator(politicsQL, 1)
    paginatorFiction1 = Paginator(fictionQL, 1)
    paginatorBooksCulture1 = Paginator(booksCultureQL, 1)
    paginatorHumourCartoons1 = Paginator(humourCartoonsQL, 1)
    paginatorPuzzleGames1 = Paginator(puzzlesGamesQL, 1)
    paginatorStyle1 = Paginator(styleQ, 1)
    try:
      all_ = paginatorall1.page(page)
      news_ = paginatorNews1.page(page)
      markets_ = paginatorMarkets1.page(page)
      politics_ = paginatorPolitics1.page(page)
      fiction_ = paginatorFiction1.page(page)
      booksCulture_ = paginatorBooksCulture1.page(page)
      humourCartoons_ = paginatorHumourCartoons1.page(page)
      puzzlesGames_ = paginatorPuzzleGames1.page(page)
      style_ = paginatorStyle1.page(page)
      

    except PageNotAnInteger:
      all_ = paginatorall.page(1)
      news_ = paginatorNews.page(1)
      markets_ = paginatorMarkets.page(1)
      politics_ = paginatorPolitics.page(1)
      fiction_ = paginatorFiction.page(1)
      booksCulture_ = paginatorBooksCulture.page(1)
      humourCartoons_ = paginatorHumourCartoons.page(1)
      puzzlesGames_ = paginatorPuzzleGames.page(1)
      style_ = paginatorStyle.page(1)
      

    except EmptyPage:
      all_ = paginatorall.page(paginatorNews.num_pages)
      news_ = paginatorNews.page(paginatorNews.num_pages)
      markets_ = paginatorMarkets.page(paginatorMarkets.num_pages)
      politics_ = paginatorPolitics.page(paginatorPolitics.num_pages)
      fiction_ = paginatorFiction.page(paginatorFiction.num_pages)
      booksCulture_ = paginatorBooksCulture.page(paginatorBooksCulture.num_pages)
      humourCartoons_ = paginatorHumourCartoons.page(paginatorHumourCartoons.num_pages)
      puzzlesGames_ = paginatorPuzzleGames.page(paginatorPuzzleGames.num_pages)
      style_ = paginatorStyle.page(paginatorStyle.num_pages)

  except:
    print("failed")

  
 

  #output  the  data in a simple form
  context = {
    'all': all,
    'news': news,       #done
    'markets': markets,   #done
    'politics': politics, #done
    'fiction': fiction,   #done
    'booksCulture': booksCulture,   #done
    'humourCartoons': humourCartoons,
    'puzzleGames': puzzlesGames,  #done
    'style': style,
    #-===========---------THE LIST VIEWS------------=======#
    'all_': all_,
    'news_': news_,       #done
    'markets_': markets_,   #done
    'politics_': politics_, #done
    'fiction_': fiction_,   #done
    'booksCulture_': booksCulture_,   #done
    'humourCartoons_': humourCartoons_,
    'puzzleGames_': puzzlesGames_,  #done
    'style_': style_,   
  }




   
  return render(request, 'home.html', context)




#THis puts all the menu items in a single page
def articlelistView(request, menu):


  TOPICS = request.GET.get('menu')
  print(TOPICS)

  # add a sorting algortithm
  topics = article.objects.order_by('slug').reverse().all().values('menu')
  print(menu)

  if topics:
    artliclelists = article.objects.filter(menu=menu)
    print('=============================================')
    print(artliclelists)
    
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

  recommendation = article.objects.filter(recommended=1)
  print(recommendation)

  context = {
    'articles': articles,
    'recommendation':recommendation,
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




