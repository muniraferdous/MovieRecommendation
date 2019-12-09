from django.db import models


class MovieSuggest(models.Model):
    genre_mood = models.CharField(max_length=55)
    item = models.CharField(max_length=1055)

    def __str__(self):
        return self.genre_mood
