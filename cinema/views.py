# cinema/views.py

from rest_framework import viewsets
from cinema.models import Movie, MovieSession
from cinema.serializers import MovieSerializer, MovieSessionSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer
