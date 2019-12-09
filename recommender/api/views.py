from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from recommender.models import MovieSuggest
from recommender.api.serializers import MovieSuggestSerializer


# @api_view(['GET',])
# def api_detail_view(request, slug):
#