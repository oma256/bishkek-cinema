from django.urls import path

from apps.api.views import (
    MovieListCreateView, 
    MovieRetrievUpdateDestroyView,
    CinemaListCreateView,
    CinemaRetrievUpdateDestroyView,
    SessionListCreateView
)


urlpatterns = [
    path('movies/', MovieListCreateView.as_view()),
    path('movies/<int:id>', MovieRetrievUpdateDestroyView.as_view()),
    path('cinemas/', CinemaListCreateView.as_view()),
    path('cinemas/<int:id>', CinemaRetrievUpdateDestroyView.as_view()),
    path('sessions/', SessionListCreateView.as_view()),
]
