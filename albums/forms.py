from django import forms
from .models import Album


class AlbumForm(forms.Form):
    title = forms.CharField(
        label="Album Title:", max_length=150, required=True)
    artist = forms.CharField(
        label="Artist Name:", max_length=150, required=True)
    genre = forms.ChoiceField(
        label="Genre:", choices=Album.Genre.choices, required=False)


class AlbumFormModel(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["title", "artist", "genre"]
