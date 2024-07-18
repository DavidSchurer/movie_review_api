from rest_framework import serializers
from .models import Movie, Review

class ReviewSerializer(serializers.ModelSerializer):
    movie_title = serializers.ReadOnlyField(source='movie.title')

    class Meta:
        model = Review
        fields = ['id', 'movie', 'movie_title', 'rating', 'review']

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields =['id', 'title', 'year', 'description']