from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

# Views
from music import views

urlpatterns = [
    # Function-based views
    #     path('', views.index, name='home'),
    #     path('top-songs', views.top_songs, name='top-songs'),
    # Class-based views
    path('', views.Index.as_view(), name='home'),
    path('top-songs', views.TopSongs.as_view(), name='top-songs'),
] 

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)