from django.db import models


# class Artist(models.Model):
#     name = models.CharField(max_length=50)

GENRE_CHOICES = []


class Album(models.Model):
    class Genre(models.TextChoices):
        ROCK = 'ROCK', 'Rock'
        ALT = 'ALT', 'Alternative'
        POP = 'POP', 'Pop'
        RAP = 'RAP', 'Hip-Hop/Rap'
        COUNTRY = 'COUNTRY', 'Country'

    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=50)
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
