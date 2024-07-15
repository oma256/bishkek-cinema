from django.contrib import admin

from .models import Movie, Cinema, Hall, Row, Place, Session


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'country', 
                    'year', 'duration', 'starring', 'picture']


@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'picture']


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ['name', 'cinema']


@admin.register(Row)
class RowAdmin(admin.ModelAdmin):
    list_display = ['number', 'hall']


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['number', 'row']


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['start_time', 'price', 'movie', 'cinema']
