from rest_framework.response import Response
from watch_list.models import Movie
from watch_list.api.serializers import MovieSerializer
#from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status


'''class MovieListAV(APIView):
    def get(self,request):
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies)
        return Response(serializer.data)
'''


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method=='GET':
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies,many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET', 'PUT','DELETE'])
def movie_deatils(request,pk):
    if request.method=='GET':
        movie=Movie.objects.get(pk=pk)
        serializer=MovieSerializer(movie)
        return Response(serializer.data)
    
    if request.method=='PUT':
        movie=Movie.objects.get(pk=pk)
        serializer=MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)



    if request.method=="DELETE":
        movie=Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)