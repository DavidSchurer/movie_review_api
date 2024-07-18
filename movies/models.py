from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()

    def __str__(self):
        return f"Review for {self.movie}: {self.rating}/5"