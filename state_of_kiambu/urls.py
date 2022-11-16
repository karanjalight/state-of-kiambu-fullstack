from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from state_of_kiambu_backend import views as views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home, name='home' ),
    path('articleview/<str:slug>' , views.articleView, name='articleview' ),
    path('articlelist/<str:menu>' , views.articlelistView, name='articlelist' ),

    path('register/', views.Signup, name= "register"),
    path('login/', auth_views.LoginView.as_view(template_name='Login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),

   
]


#this url maps images to the front end

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 