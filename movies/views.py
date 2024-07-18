# movie_review_api\movies\views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from rest_framework.pagination import PageNumberPagination

class MovieListCreate(APIView):
    def get(self, request):
        # Retrive the movies from the database
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        # Deserialize the movie data
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewCreate(APIView):
    pagination_class = None
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
