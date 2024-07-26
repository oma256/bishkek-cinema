from typing import Any

from django.views.generic import TemplateView

from apps.cinemas.models import Cinema, Hall, Place, Row, Session


class CinemaListView(TemplateView):
    template_name = 'cinemas/cinemas.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        data['cinemas'] = Cinema.objects.all()

        return data


class SessionListView(TemplateView):
    template_name = 'cinemas/sessions.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        cinema_id = self.kwargs.get('cinema_id')
        cinema = Cinema.objects.filter(pk=cinema_id).first()
        data['sessions'] = Session.objects.filter(cinema_id=cinema.id)

        return data


class SessionDetailView(TemplateView):
    template_name = 'cinemas/session_detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        session_id = self.kwargs.get('session_id')
        session = Session.objects.filter(id=session_id).first()
        rows = []
        rows_list = Row.objects.filter(hall_id=session.hall_id)
        
        for row in rows_list:
            places = Place.objects.filter(row_id=row.id)
            temp = []
            for place in places:
                temp.append({'row': row.number, 'seat': place.number})
            rows.append(temp)

        data['session'] = session
        data['rows'] = rows

        return data
