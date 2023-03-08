from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Artist
from .forms import AlbumForm
from django.utils.text import slugify


def album_list(request):
    albums = Album.objects.all().order_by("title")
    return render(request, 'albums/album_list.html',
                  {'albums': albums, 'title': 'All Albums'})


def album_new(request, album=None):
    print(request)
    if request.method == 'POST':
        # if the page is reloading with data passed through the form
        form = AlbumForm(request.POST, request.FILES)

        # bind it to the albumform
        print(form.is_valid)
        print(request)
        print(form.errors)

        if form.is_valid():
            tit = form.cleaned_data['title']
            gen = form.cleaned_data['genre']
            artwork = request.FILES['artwork']

            art, new = Artist.objects.get_or_create(
                name=form.cleaned_data['artist'])

            art.slug = slugify(art.name, True) if new else None

            album = Album.objects.create(
                title=tit, genre=gen, artist=art, artwork=artwork)
            print(album)
            breakpoint()
            return redirect('album_details', pk=album.pk)
    form = AlbumForm()

    return render(request, 'albums/album_edit.html', {'form': form})


def album_details(request, pk):
    album = get_object_or_404(Album, pk=pk)

    return render(request, 'albums/album_details.html', {'album': album})


def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)

    if request.method == 'POST':
        # if the page is reloading with edited data passed through the form
        form = AlbumForm(request.POST, request.FILES)
        print(form.is_valid)
        # bind it to the albumform
        if form.is_valid():
            album.title = form.cleaned_data['title']
            album.genre = form.cleaned_data['genre']

            art, new = Artist.objects.get_or_create(
                name=form.cleaned_data['artist'])

            album.artist = art

            album.artwork = request.FILES['artwork']  # form.instance

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


def artist_list(request, slug):
    artist = Artist.objects.get(slug=slug)
    albums = Album.objects.filter(artist=artist)
    return render(request, 'albums/album_list.html',
                  {'albums': albums, 'title': f'{artist.name} Albums'})  # THIS IS WHERE YOU LEFT OFF


def album_delete(request, pk):
    Album.objects.get(pk=pk).delete()
    return redirect(request, 'albums/album_list.html')
