from django.http import JsonResponse
from django.shortcuts import render

from services import IMDBService
from .models import Movie


def top_movies(request):
    movies = Movie.objects.all()

    context = {
        'movies': movies
    }
    return render(request, template_name='core/movies.html', context=context)


def scrape_data(request):
    category = request.GET['category']
    service = IMDBService.get_service(category=category)
    objects = service.get_objects()
    data = service.persist_objects(objects)

    return JsonResponse({'data': data})