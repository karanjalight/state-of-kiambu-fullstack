from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from state_of_kiambu_backend import views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home, name='home' ),
    path('articleview/' , views.articleView, name='home' ),
    path('articlelist/' , views.articlelistView, name='home' ),
    


]



""" if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) """