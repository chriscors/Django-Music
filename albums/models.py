from django.db import models


# class Artist(models.Model):
#     name = models.CharField(max_length=50)


class Album(models.Model):
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=50)
    # artist = models.ForeignKey(
    #     Artist, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
