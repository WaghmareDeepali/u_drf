from rest_framework.response import Response
from watch_list.models import Movie
from watch_list.api.serializers import MovieSerializer

def movie_list(request):
    movies=Movie.objects.all()
    serializer=MovieSerializer(movies)
    return Response(serializer.data)

def movie_deatils(request,pk):
    movie=Movie.objects.get(pk=pk)
    serializer=MovieSerializer(movie)
    return Response(serializer.data)
