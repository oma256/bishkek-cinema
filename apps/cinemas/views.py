from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView

from apps.cinemas.models import Cinema, Movie, Session


class CinemaListView(ListView):
    template_name = 'cinemas/cinemas.html'
    queryset = Cinema.objects.all()
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        data['cinemas'] = self.queryset

        return data


class SessionListView(ListView):
    template_name = 'cinemas/sessions.html'
    model = Cinema
    context_object_name = 'cinema'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        cinema_id = self.kwargs.get('pk')
        cinema = Cinema.objects.filter(pk=cinema_id).first()
        data['sessions'] = Session.objects.filter(cinema_id=cinema.id)
    
        print(data['sessions'])
    
        return data


class SessionDetailView(DetailView):
    model = Session
    template_name = 'cinemas/session_detail.html'
    context_object_name = 'session'
