from rest_framework import serializers
from .models import Movie, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'movie', 'rating', 'review']

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields =['id', 'title', 'year', 'description']