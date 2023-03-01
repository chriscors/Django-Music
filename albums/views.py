from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Artist
from .forms import AlbumForm


def album_list(request):
    albums = Album.objects.all().order_by("title")
    return render(request, 'albums/album_list.html', {'albums': albums})


def album_new(request):
    print(request.method)
    if request.method == 'POST':
        # if the page is reloading with data passed through the form
        form = AlbumForm(request.POST)

        # bind it to the albumform
        if form.is_valid():
            tit = form.cleaned_data['title']
            gen = form.cleaned_data['genre']

            art, new = Artist.objects.get_or_create(
                name=form.cleaned_data['artist'])

            Album.objects.create(title=tit, genre=gen, artist=art)
        # return redirect()  # finish filling this out
    form = AlbumForm()

    return render(request, 'albums/album_edit.html', {'form': form})


def album_details(request, pk):
    album = get_object_or_404(Album, pk=pk)

    return render(request, 'albums/album_details.html', {'album': album})


def album_edit(request, pk):
    return render(request, 'albums/album_edit.html')
