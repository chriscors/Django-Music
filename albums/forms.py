from django import forms
from .models import Album


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ["title", "artist", "genre"]
        # widgets = {
        #     'title': forms.CharField(attrs={'class': 'input'})
        # }
