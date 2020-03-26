from django.contrib import admin
from django.urls import include, path
import music

# Views
from artist import views

app_name = "artist"
urlpatterns = [
    path("create-artist/", views.createArtist.as_view(), name="createArtist"),

    
  
]