import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_theater_booking.settings")
django.setup()

def before_all(context):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_theater_booking.settings")
    django.setup()

    # Allow Django test client host
    from django.conf import settings
    settings.ALLOWED_HOSTS.append("testserver")

# Added this as a supplement to making a full test database
TEST_PREFIX = "behave__"

def after_scenario(context, scenario):
    from bookings.models import Movie, Showing, Seat, Booking
    from django.contrib.auth.models import User

    # delete only behave-created rows
    Booking.objects.filter(seat__seat_number__startswith=TEST_PREFIX).delete()
    Seat.objects.filter(seat_number__startswith=TEST_PREFIX).delete()
    Showing.objects.filter(movie__title__startswith=TEST_PREFIX).delete()
    Movie.objects.filter(title__startswith=TEST_PREFIX).delete()
    User.objects.filter(username__startswith=TEST_PREFIX).delete()