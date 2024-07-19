from django.urls import path
from .views import CinemaListView, SessionListView, SessionDetailView


app_name = 'cinemas'


urlpatterns = [
    path('', CinemaListView.as_view(), name='index'),
    path('cinemas/<int:cinema_id>/', SessionListView.as_view(), name='sessions'),
    path('cinemas/<int:cinema_id>/sessions/<int:session_id>', 
         SessionDetailView.as_view(), 
         name='session_detail'),
]
