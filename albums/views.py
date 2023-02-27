from django.shortcuts import render
from .models import Album


def album_list(request):
    albums = Album.objects.order_by('creation_date')
    render(request, 'blog/album_list.html', {'albums', albums})
