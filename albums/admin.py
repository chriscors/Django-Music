from django.contrib import admin
from .models import Album, Artist


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'genre')


admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist)
