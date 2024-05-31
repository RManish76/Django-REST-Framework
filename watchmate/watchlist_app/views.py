# will use api foldere views.py instead of app folder views.py

'''
from django.shortcuts import render
from . import models
from django.http import JsonResponse

# Create your views here.

def movie_list(request):
    movies = models.Movie.objects.all()
    #print(list(movies.values()))
    print(movies.name)
    data = {
        'movies': list(movies.values())
        }

    return JsonResponse(data)

def movie_details(request, pk):
    movie = models.Movie.objects.get(pk=pk)
    data = {
        'name': movie.name,
        'description':movie.description,
        'active': movie.active
    }
    # Here we cannot use .values() method becasue .get() return single modle instace.
    # And for single model instace .value() is not available.
    # .value() is only available for QuerySet Object.
    # so we can only access data using attributes like movie.name or movie.status etc
    return JsonResponse(data)
'''