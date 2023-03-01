from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm


def album_list(request):
    albums = Album.objects.all().order_by("title")
    return render(request, 'albums/album_list.html', {'albums': albums})


def album_new(request):
    if request.method == 'POST':
        # if the page is reloading with data passed through the form
        form = AlbumForm(request.post)
        # bind it to the albumform
        if form.is_valid():
            form.save()
        return redirect()  # finish filling this out
    form = AlbumForm
    return render(request, 'albums/album_edit.html', {'form': form})
