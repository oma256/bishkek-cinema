from typing import Any

from django.views.generic import TemplateView

from apps.cinemas.models import Cinema, Hall, Place, Row, Session
from apps.orders.models import Order


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
                order = Order.objects.filter(session_id = int(session_id), 
                                             row_id = row.id,
                                             place_id = place.id).first()

                if order:
                    temp.append({
                        'row': row.number, 
                        'seat': place.number,
                        'row_id': row.id,
                        'seat_id': place.id,
                        'disabled': True
                    })
                else:
                    temp.append({
                        'row': row.number, 
                        'seat': place.number,
                        'row_id': row.id,
                        'seat_id': place.id,
                        'disabled': False
                    })

            rows.append(temp)

        data['session'] = session
        data['rows'] = rows

        return data


class MovieListView(TemplateView):
    template_name = 'cinemas/movies.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        sessions = Session.objects.select_related('movie').distinct('movie')
        data['sessions'] = sessions

        return data


class CinemaSessionListView(TemplateView):
    template_name = 'cinemas/cinemas.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        movie_id = self.kwargs.get('movie_id')
        cinemas = Cinema.objects.filter(session__isnull=False, 
                                        session__movie_id=movie_id).distinct()
        data['cinemas'] = cinemas

        return data


class OrderListView(TemplateView):
    template_name = 'cinemas/orders.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        data['orders'] = Order.objects.filter(user__id = user_id)

        return data
