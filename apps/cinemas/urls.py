from django.urls import path
from .views import (
    CinemaListView, 
    CinemaSessionListView, 
    MovieListView, 
    SessionListView, 
    SessionDetailView,
    OrderListView,
)


app_name = 'cinemas'


urlpatterns = [
    path('', CinemaListView.as_view(), name='index'),
    path('cinemas/<int:cinema_id>/', SessionListView.as_view(), name='sessions'),
    path('cinemas/<int:cinema_id>/sessions/<int:session_id>', 
         SessionDetailView.as_view(), 
         name='session_detail'),
    path('movies/', MovieListView.as_view(), name='movies'),
    path('movies/<int:movie_id>/cinemas/<int:cinema_id>', 
         CinemaSessionListView.as_view(), name='cinema_sessions'),
    path('orders', OrderListView.as_view(), name='orders'),
]
