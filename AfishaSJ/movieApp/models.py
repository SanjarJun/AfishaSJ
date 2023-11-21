from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Director(models.Model):
    name = models.CharField(verbose_name="Director name", max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(verbose_name="Movie title", max_length=255)
    description = models.CharField(verbose_name="Movie description", max_length=255)
    duration = models.SmallIntegerField(
        verbose_name="Movie duration",
        validators=[MinValueValidator(limit_value=40, message="Длительность фильма должна быть не менее 30 мин")]
    )
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.CharField(verbose_name="Review text", max_length=255)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
# password = root
