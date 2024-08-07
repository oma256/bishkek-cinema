from rest_framework.serializers import ModelSerializer

from apps.cinemas.models import Cinema, Hall, Movie, Session


class MovieSerializer(ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'name', 'description', 'country', 'year', 'duration',
                  'starring', 'picture', 'genre']


class CinemaSerializer(ModelSerializer):

    class Meta:
        model = Cinema
        fields = ['id', 'name', 'picture', 'address']


class HallSerializer(ModelSerializer):

    class Meta:
        model = Hall
        fields = ['id', 'name']

class SessionSerializer(ModelSerializer):
    movie = MovieSerializer()
    cinema = CinemaSerializer()
    hall = HallSerializer()

    class Meta:
        model = Session
        fields = ['id', 'start_time', 'price', 'movie', 'cinema', 'hall']