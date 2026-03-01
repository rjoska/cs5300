from django.contrib import admin
from .models import Movie, Showing, Seat, Booking

admin.site.register(Movie)
admin.site.register(Showing)
admin.site.register(Seat)
admin.site.register(Booking)