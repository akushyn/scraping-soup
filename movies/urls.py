from django.urls import path
from .views import top_movies


urlpatterns = [
    path('movies/', top_movies, name='movies')
]
