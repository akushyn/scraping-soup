from django.urls import path
from .views import top_movies, scrape_data

urlpatterns = [
    path('', top_movies, name='movies'),
    path('scrape_data/', scrape_data, name='scrape_data')
]
