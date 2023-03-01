from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Album(models.Model):
    class Genre(models.TextChoices):
        ROCK = 'Rock', 'Rock'
        ALT = 'Alt', 'Alternative'
        POP = 'Pop', 'Pop'
        RAP = 'Rap', 'Hip-Hop/Rap'
        COUNTRY = 'Country', 'Country'

    title = models.CharField(max_length=250)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.CharField(
        max_length=8,
        choices=Genre.choices,
        default="---------"
    )
    # artist = models.ForeignKey(
    #     Artist, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
