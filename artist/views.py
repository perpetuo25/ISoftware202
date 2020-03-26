from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from music.models import Artist
from django.contrib.auth import authenticate


from artist.forms import AddArtist


class createArtist(View):
    template = "artist/create-artist.html"
    def get(self,request):
        form = AddArtist()
        context = {"form" : form}
        return render(request, self.template, context)

    def post(self, request):
        form = AddArtist(request.POST)
        context = {"form" : form}
        if form.is_valid():
           print("hola")
           artist = Artist.objects.create(
            name=form.cleaned_data["name"],
            image=form.cleaned_data["image"],
        )
        return render(request, self.template,context)

# Create your views here.
