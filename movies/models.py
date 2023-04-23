from django.db import models


class Movie(models.Model):
    poster_image = models.URLField()
    title = models.CharField(max_length=250)
    year = models.IntegerField()
    rating = models.FloatField()

    def __repr__(self):
        return f"{self.title} ({self.year})"
