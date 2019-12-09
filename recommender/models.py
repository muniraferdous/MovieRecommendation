from django.db import models


class MovieSuggest(models.Model):
    # title = models.CharField(max_length=255)
    # year = models.CharField(max_length=4)
    # imdb_id = models.CharField(max_length=55)
    # poster_path = models.CharField(max_length=2055)
    mood = models.CharField(max_length=55)

    def __str__(self):
        return self.mood
