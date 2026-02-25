from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
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

# I have seen you can either make a seperate file for this or you can just add these tests here as well
# Reference: https://www.django-rest-framework.org/api-guide/testing/, https://medium.com/@akshatgadodia/testing-django-and-django-rest-framework-drf-ensuring-reliability-236f0fcbeee6
# I also used ChatGPT as sources are lacking for API tests
class APITests(APITestCase):
    #I think I need to redo the setup again which is not optimal but this is fine for now
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="API1", password="API1testpass67")
        self.movie = Movie.objects.create(
            title="THE API MOVIE",
            description="Sci-fi tech-pic",
            release_date="2025-02-25",
            duration=222
        )
        self.showing = Showing.objects.create(
            movie=self.movie,
            start_time=timezone.now()
        )
        self.seat = Seat.objects.create(
            showing=self.showing,
            seat_number="AP12",
            booking_status=False
        )
    
    def test_movie_page_200(self):
        response = self.client.get("/api/movies/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)

    
    def test_seat_page_200(self):
        response = self.client.get("/api/seats/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        self.assertIn("booking_status", data[0])
    
    def test_showing_page_200(self):
        response = self.client.get("/api/showings/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        self.assertIn("start_time", data[0])

    def test_booking_403_when_no_user(self):
        response = self.client.get("/api/bookings/")
        self.assertEqual(response.status_code, 403)

    def test_booking_page_200_when_logged_in(self):
        self.client.login(username="API1", password="API1testpass67")
        response = self.client.get("/api/bookings/")
        self.assertEqual(response.status_code, 200)

    def test_create_booking_marks_seat_booked(self):
        self.client.login(username="API1", password="API1testpass67")
        #ChatGPT helped me make this as I wanted to test the post, but onlne examples were lacking
        response = self.client.post("/api/bookings/", {"seat": self.seat.id}, format="json")
        self.assertEqual(response.status_code, 201)

        self.seat.refresh_from_db()
        self.assertTrue(self.seat.booking_status)

        self.assertTrue(Booking.objects.filter(user=self.user, seat=self.seat).exists())