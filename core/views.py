from django.shortcuts import render
from movies.models import Movie
from services import ScrapeMoviesService


def index(request):

    service = ScrapeMoviesService()
    top_movies = service.get_top_movies()

    top_movies = []
    for top_movie in top_movies:
        movie = (
            Movie.objects
            .filter(
                title=top_movie.get('title'),
                year=top_movie.get('year')
            )
            .first()
        )
        if movie:
            movie.poster_image = top_movie.get('poster_image')
            movie.rating = top_movie.get('rating')
            movie.save()
        else:
            movie = Movie(
                poster_image=top_movie.get('poster_image'),
                title=top_movie.get('title'),
                year=top_movie.get('year'),
                rating=top_movie.get('rating'),
            )
            movie.save()

    return render(request, 'core/index.html')
