from rest_framework import serializers
from recommender.models import MovieSuggest


class MovieSuggestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSuggest
        fields = ['title', 'year', 'imdb_id', 'poster_path']
