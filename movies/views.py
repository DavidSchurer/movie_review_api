from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Movie, Review
import json

def add_review(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        movie, created = Movie.objects.get_or_create(title=data['movie'])
        review = Review(movie=movie, rating=data['rating'], review=data['review'])
        review.save()
        return JsonResponse({'status': 'success'}, status=201)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def get_reviews(request, movie_title):
    try:
        movie = Movie.objects.get(title=movie_title)
        reviews = movie.reviews.all()
        reviews_data = [{'rating': review.rating, 'review': review.review} for review in reviews]
        return JsonResponse(reviews_data, safe=False)
    except Movie.DoesNotExist:
        return JsonResponse([], safe=False)