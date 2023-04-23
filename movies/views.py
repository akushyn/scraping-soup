from django.shortcuts import render
from .models import Movie


def top_movies(request):
    movies = Movie.objects.all()

    context = {
        'movies': movies
    }
    return render(request, template_name='core/movies.html', context=context)
