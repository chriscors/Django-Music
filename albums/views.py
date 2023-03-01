from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Artist
from .forms import AlbumForm


def album_list(request):
    albums = Album.objects.all().order_by("title")
    return render(request, 'albums/album_list.html', {'albums': albums})


def album_new(request, album=None):
    if request.method == 'POST':
        # if the page is reloading with data passed through the form
        form = AlbumForm(request.POST)

        # bind it to the albumform
        if form.is_valid():
            tit = form.cleaned_data['title']
            gen = form.cleaned_data['genre']

            art, new = Artist.objects.get_or_create(
                name=form.cleaned_data['artist'])

            album = Album.objects.create(title=tit, genre=gen, artist=art)
        return redirect('album_detail', pk=album.pk)
    form = AlbumForm()

    return render(request, 'albums/album_edit.html', {'form': form})


def album_details(request, pk):
    album = get_object_or_404(Album, pk=pk)

    return render(request, 'albums/album_details.html', {'album': album})


def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    print(album)
    if request.method == 'POST':
        # if the page is reloading with edited data passed through the form
        form = AlbumForm(request.POST)

        # bind it to the albumform
        if form.is_valid():
            album.title = form.cleaned_data['title']
            album.genre = form.cleaned_data['genre']

            art, new = Artist.objects.get_or_create(
                name=form.cleaned_data['artist'])

            album.artist = art

            album.save()
        return redirect('album_details', pk=album.pk)
    # Else load in saved data to edited
    form = AlbumForm(initial={
        'title': album.title,
        'artist': album.artist,
        'genre': album.genre,
    })
    # print(album.title, album.artist)
    # form.title = album.title
    # form.artist = album.artist
    # form.genre = album.genre
    return render(request, 'albums/album_edit.html', {'form': form})


def artist_list(request, artist):
    albums = Album.objects.get(artist=artist)
    return render(request, 'albums/artist_list.html',
                  {'albums': albums, 'title': f'{albums[0].artist} Albums'})  # THIS IS WHERE YOU LEFT OFF
