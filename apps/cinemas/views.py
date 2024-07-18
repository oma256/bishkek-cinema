from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView

from apps.cinemas.models import Cinema, Session


class CinemaListView(ListView):
    template_name = 'cinemas/index.html'
    queryset = Cinema.objects.all()
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        data['cinemas'] = self.queryset

        return data


class CinemasDetailView(DetailView):
    template_name = 'cinemas/cinema_detail.html'
    model = Cinema
    context_object_name = 'cinema'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        cinema = Cinema.objects.filter(pk=pk)
        return cinema

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        cinema_id = self.kwargs.get('pk')
        cinema = Cinema.objects.filter(pk=cinema_id).first()
        data['sessions'] = Session.objects.filter(cinema_id=cinema.id)

        return data
