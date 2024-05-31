from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app import models
from . import serializers

@api_view() #by default api_view() decorator is set to get. we can use @api_view(['GET','POST']) for extra methods
def movie_list(request):
    movies = models.Movie.objects.all()
    serializer = serializers.MovieSerializer(movies, many=True)
    """
    variable name can be anything it is not mandatory to use serializer as variable name.
    serializers work on only single object of QuerySet but here we are passing .all()
    in movies vairable which is fetching mutliple objects within a QuerySet.
    That's the reason we need to set the serializer many=True, so that it'll know it might get
    mutliptle objects so it need to traverse to each object.
    """
    return Response(serializer.data)
    """
    now serializer has converted the data  but it's still a object and to access that data
    we need to user attribute like we used previously movies.name. movies.active etc
    but instead of accessing one by one we can just now say serializer.data it'll get all fields data for us. 
    """

@api_view()
def movie_details(request, pk):
    movie = models.Movie.objects.get(pk=pk)
    serializer = serializers.MovieSerializer(movie)
    return Response(serializer.data)
    """
    now serializer has converted the data  but it's still a object and to access that data
    we need to user attribute like we used previously movies.name. movies.active etc
    but instead of accessing one by one we can just now say serializer.data it'll get all fields data for us. 
    """
