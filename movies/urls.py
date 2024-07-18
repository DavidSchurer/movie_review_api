from django.urls import path
from .views import MovieListCreate, ReviewCreate

urlpatterns = [
    path('movies/', MovieListCreate.as_view(), name='movie-list-create'),
    path('reviews/', ReviewCreate.as_view(), name='review-create'),
]