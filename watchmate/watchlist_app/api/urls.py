from django.urls import path
from . import views

urlpatterns=[
    # path('list/',views.movie,name='movie_list'),
    # path('<int:pk>',views.movie_details,name='movie_details'),
    path('list/',views.MovieListAPIView.as_view(),name='movie_list'),
    path('<int:pk>/',views.MovieDetailAPIView.as_view(),name='movie_detail'),
]