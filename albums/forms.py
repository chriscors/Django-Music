from django import forms
from .models import Album


class AlbumForm(forms.Form):
    title = forms.CharField(
        label="Album Title:", max_length=150, required=True)
    artist = forms.CharField(
        label="Artist Name:", max_length=150, required=True)
    genre = forms.ChoiceField(
        label="Genre:", choices=Album.Genre.choices, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'input'
        # self.fields['title'].label.widget.attrs['class'] = 'label'

        self.fields['artist'].widget.attrs['class'] = 'input'
        # self.fields['artist'].label.widget.attrs['class'] = 'label'

        self.fields['genre'].widget.attrs['class'] = 'select'
        # self.fields['genre'].label.widget.attrs['class'] = 'label'


class AlbumFormModel(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["title", "artist", "genre"]
