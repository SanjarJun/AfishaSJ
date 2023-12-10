from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

# Create your models here.
class Director(models.Model):
    name = models.CharField(verbose_name="Director name", max_length=255)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(verbose_name="Movie title", max_length=255)
    description = models.CharField(verbose_name="Movie description", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    duration = models.SmallIntegerField(
        verbose_name="Movie duration",
        validators=[MinValueValidator(limit_value=40, message="Length of the movie must be longer than 30 mins")]
    )
    director = models.ForeignKey(Director, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def count_reviews(self):
        return self.review.all().count()

    def all_reviews(self):
        reviews = Review.objects.filter(movie=self)
        return [{'id': i.id, 'stars': i.stars} for i in reviews]

    @property
    def avg_reviews(self):
        reviews = Review.objects.filter(movie=self)
        res = [int(i.stars) for i in reviews]

        return round(sum(res) / len(res))


class Review(models.Model):
    stars = models.CharField(verbose_name="Review rating")
    text = models.CharField(verbose_name="Review text", max_length=255)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='review')

    def __str__(self):
        return self.text
# password = root
