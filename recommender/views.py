from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json

from .movie import build_chart
from .models import MovieSuggest
from .retrieve_genre import retrieve_genre


def home_view(request):
    if request.is_ajax():
        if request.method == 'POST':
            name = request.POST['name']
            if name == 'emotion':
                datas = request.POST['emotion']
                obj = MovieSuggest(genre_mood='mood', item=datas)
                obj.save()
            else:
                genres = request.POST['emotion']
                # data = json.loads(genres)
                # print(len(data))
                obj = MovieSuggest(genre_mood='genre', item=genres)
                obj.save()
                # if len(data):
                #     obj = MovieSuggest(mood=data)
                #     obj.save()
            return HttpResponse("ok")
    return render(request, 'home.html', {})


def result_view(request):
    qs = MovieSuggest.objects.last()
    print(qs.genre_mood)

    if qs.genre_mood == 'mood':
        qs.item = retrieve_genre(qs.item)
    print(qs.item.title())
    result = build_chart(qs.item.title())
    titles = []
    years = []
    imdb_ids = []
    poster_paths = []
    dic = {}

    for title in result['title']:
        titles.append(title)

    for year in result['year']:
        years.append(year)

    for imdb_id in result['imdb_id']:
        imdb_ids.append(imdb_id)

    for poster_path in result['poster_path']:
        poster_paths.append(poster_path)

    for i in range(24):
        dic[i] = {
            'title': titles[i],
            'year': years[i],
            'imdb_id': imdb_ids[i],
            'poster_path': poster_paths[i],
        }

    context = {
        'dic': dic
    }

    return render(request, 'toot.html', context)
