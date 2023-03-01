from django.shortcuts import render, redirect
from .models import Album, Artist
from .forms import AlbumForm


def album_list(request):
    albums = Album.objects.all().order_by("title")
    return render(request, 'albums/album_list.html', {'albums': albums})


def album_new(request):
    if request.method == 'POST':
        # if the page is reloading with data passed through the form
        form = AlbumForm(request.POST)
        # bind it to the albumform
        if form.is_valid():
            Album.title = form.cleaned_data['title']
            Album.genre = form.cleaned_data['genre']

            artist, new = Artist.objects.get_or_create(
                name=form.cleaned_data['artist'])

            Album.artist = artist

            form.save()
        # return redirect()  # finish filling this out
    form = AlbumForm
    return render(request, 'albums/album_edit.html', {'form': form})
