from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Movie, Showing, Seat, Booking

# Create your tests here.
# https://docs.djangoproject.com/en/6.0/topics/testing/overview/ 
class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="u1", password="u1testpass67")
        self.movie = Movie.objects.create(
            title="THE MOVIE",
            description="Sci-fi bio-pic",
            release_date="2025-02-24",
            duration=212
        )
        self.showing = Showing.objects.create(
            movie=self.movie,
            start_time=timezone.now()
        )
        self.seat = Seat.objects.create(
            showing=self.showing,
            seat_number="AP11",
            booking_status=False
        )
    
    # Make sure each object loads correct
    def test_movie_str(self):
        self.assertEqual(str(self.movie), "THE MOVIE")

    def test_showing_str(self):
        self.assertIn("THE MOVIE", str(self.showing))

    def test_seat_str(self):
        self.assertIn("AP11", str(self.seat))

    def test_booking_str(self):
        booking = Booking.objects.create(seat=self.seat, user=self.user)
        self.assertIn("u1", str(booking))