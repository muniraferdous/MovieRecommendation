from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json

from .movie import build_chart
from .models import MovieSuggest


def home_view(request):
    if request.is_ajax():
        if request.method == 'POST':
            name = request.POST['name']
            # data = []
            # titles = []
            # years = []
            # imdb_ids = []
            # poster_paths = []
            # dic = {}
            if name == 'emotion':
                datas = request.POST['emotion']
                obj = MovieSuggest(mood=datas)
                obj.save()
            else:
                genres = request.POST['genre']
                data = json.loads(genres)
                result = build_chart(data[0])
                title = result['title'][0]
                print(data[0])

            return HttpResponse("ok")
    return render(request, 'home.html', {})


def result_view(request):
    qs = MovieSuggest.objects.last()
    print(qs.mood)

    result = build_chart('Romantic')

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
    # data = json.dumps(dic)
    # print(data)
    # return JsonResponse(data)

    context = {
        'dic': dic
    }

    return render(request, 'toot.html', context)