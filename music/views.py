from django.shortcuts import render, redirect
from django.views import View
from .models import Song, Artist


def index(request):
    template = "music/index.html"
    return render(request, template)
   
def top_songs(request):

    
    template = "music/top_songs.html"
    return render(request, template)

class Index(View):
    """Music index.
    Showing some artists, songs, albums and playlists.
    TODO: Show artists.
    TODO: Show songs.
    TODO: Show albums.
    TODO: Show playlists.
    """

    template = "music/index.html"

    def get(self, request):
        """GET method."""
        return render(request, self.template)


class TopSongs(View):
    """Top songs.
    TODO: Show songs by its popularity.
    """

    template = "music/top_songs.html"

    def get(self, request):
        """GET method."""
        songs = Song.objects.all()
        image = Artist.objects.all()
        print(songs)
        print(image)
        return render(request, self.template, {"songs": songs,"image":image})