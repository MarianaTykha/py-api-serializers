from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, MovieSessionViewSet


router = DefaultRouter()
router.register(r"movies", MovieViewSet)
router.register(r"movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
