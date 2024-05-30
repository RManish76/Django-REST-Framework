from django.shortcuts import render
from . import models
from django.http import JsonResponse

# Create your views here.

def movie_list(request):
    movies = models.Movie.objects.all()
    #print(list(movies.values()))
    data = {
        'movies': list(movies.values())
        }

    return JsonResponse(data)
