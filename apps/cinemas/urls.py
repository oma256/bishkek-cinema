from django.urls import path
from .views import CinemaListView, CinemasDetailView


app_name = 'cinemas'


urlpatterns = [
    path('', CinemaListView.as_view(), name='index'),
    path('<int:pk>/', CinemasDetailView.as_view(), name='detail')
]
