from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from music.models import Artist


class AddArtist(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('name','image',)
    def cleanName(self):
        """Validate that the email doesn't exist in the database.
        Just validating email field.
        """
        data = self.cleaned_data["name"]
        if Artist.objects.filter(name=data).count() > 0:
            raise forms.ValidationError("This artist already exists.")

        return data


    def cleanImage(self):
        """Validate that the email doesn't exist in the database.
        Just validating email field.
        """
        image = self.cleaned_data.get('image', True)
        if Artist.objects.filter(image = image).count()>0 :
             raise forms.ValidationError("This artist already exists.")


        return data  