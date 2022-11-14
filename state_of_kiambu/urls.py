from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from state_of_kiambu_backend import views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home, name='home' ),
    path('articleview/<str:slug>' , views.articleView, name='articleview' ),
    path('articlelist/<str:menu>' , views.articlelistView, name='articlelist' ),
]


#this url maps images to the front end

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 