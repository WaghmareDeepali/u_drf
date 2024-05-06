from django.shortcuts import render
from watch_list.models import Movie
from django.http import JsonResponse

'''# Create your views here.
def movie_list(request):
    movies=Movie.objects.all()
    data={'Movies':list(movies.values())}

    return JsonResponse(data)


def movie_deatils(request,pk):
    movie=Movie.objects.get(pk=pk)
    data={
        'name':movie.name,
        'description':movie.description,
        'active':movie.active
    }
    print(movie)
    return JsonResponse(data)
'''