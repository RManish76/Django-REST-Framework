from rest_framework.response import Response
from rest_framework import status
#from rest_framework.decorators import api_view   #for function based view
from rest_framework.views import APIView          #for class based view
from watchlist_app import models
from . import serializers


#==========================Class Based View===========================
class MovieListAPIView(APIView): #for all data

    # Get method using APIView class   -> no need to write if like function based
    def get(self, request):
        movies = models.Movie.objects.all()
        serializer = serializers.MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class MovieDetailAPIView(APIView): #for specific data

    def get(self, request, pk):
        try:
            movie = models.Movie.objects.get(pk=pk)
        except models.Movie.DoesNotExist:
            return Response({'error': 'Movie nof found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = serializers.MovieSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = models.Movie.objects.get(pk=pk)
        serializer = serializers.MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        movie = models.Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)










# =================Function Based View==========================

# @api_view(['GET','POST']) #by default api_view() decorator is set to get. we can use @api_view(['GET','POST']) for extra methods
# def movie_list(request):
#     if request.method =='GET':
#         movies = models.Movie.objects.all()
#         serializer = serializers.MovieSerializer(movies, many=True)
#         """
#         variable name can be anything it is not mandatory to use serializer as variable name.
#         serializers work on only single object of QuerySet but here we are passing .all()
#         in movies vairable which is fetching mutliple objects within a QuerySet.
#         That's the reason we need to set the serializer many=True, so that it'll know it might get
#         mutliptle objects so it need to traverse to each object.
#         """
#         return Response(serializer.data)
#         """
#         now serializer has converted the data  but it's still a object and to access that data
#         we need to user attribute like we used previously movies.name. movies.active etc
#         but instead of accessing one by one we can just now say serializer.data it'll get all fields data for us. 
#         """ 
    
#     if request.method == 'POST':
#         serializer = serializers.MovieSerializer(data=request.data)
#         #created a serializer object from recieved data

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def movie_details(request, pk):
#     if request.method == 'GET':
#         try:
#             movie = models.Movie.objects.get(pk=pk)
#         except models.Movie.DoesNotExist:
#             return Response({'Error':'Movie does not exist'},status=status.HTTP_404_NOT_FOUND)
#         serializer = serializers.MovieSerializer(movie)

#         return Response(serializer.data)
#         """
#         now serializer has converted the data  but it's still a object and to access that data
#         we need to user attribute like we used previously movies.name. movies.active etc
#         but instead of accessing one by one we can just now say serializer.data it'll get all fields data for us. 
#         """
    
#     if request.method == 'PUT':
#         movie = models.Movie.objects.get(pk=pk) 
#         serializer = serializers.MovieSerializer(movie, data=request.data) 
#         #created a serializer object from recieved data for the object which we have passed.
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

#     if request.method == 'DELETE':
#         movie = models.Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

