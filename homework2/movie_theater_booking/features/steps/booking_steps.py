from behave import given, when, then
from django.test import Client
from django.utils import timezone
from django.contrib.auth.models import User
from bookings.models import Movie, Showing, Seat, Booking
import uuid

TEST_PREFIX = "behave__"

@given("I am on the movies page")
def go_movies(context):
    context.client = Client()
    context.response = context.client.get("/movies-page/")

@given("I am on the home page")
def go_home(context):
    context.client = Client()
    context.response = context.client.get("/")

@given("I am on the showings page")
def go_movies(context):
    context.client = Client()
    context.response = context.client.get("/movies/1/showings/")

@given("I am on the seats page")
def go_movies(context):
    context.client = Client()
    context.response = context.client.get("/showings/3/seats/")

@then('I should see "{text}"')
def should_see_text(context, text):
    assert context.response.status_code == 200
    assert text.encode() in context.response.content

@given("I am not logged in")
def not_logged_in(context):
    context.client = Client()

@given("there is an available seat for the behave movie")
def create_seat(context):
    # CHat GPT helped me make the tag and prefix idea
    tag = uuid.uuid4().hex[:8]
    context.tag = tag

    movie = Movie.objects.create(
        title=f"{TEST_PREFIX}Movie_{tag}",
        description="behave test movie",
        release_date="2026-01-01",
        duration=100,
    )
    showing = Showing.objects.create(movie=movie, start_time=timezone.now())

    context.seat = Seat.objects.create(
        showing=showing,
        seat_number="Z9",
        booking_status=False,
    )

@given("I am logged in as a user")
def logged_in(context):
    context.client = Client()
    context.user = User.objects.create_user(
        username=f"{TEST_PREFIX}user_{context.tag}",
        password="pass12345"
    )
    context.client.force_login(context.user)

@when("I visit my booking history page")
def visit_booking_history(context):
    context.response = context.client.get("/bookings-page/", follow=False)

@when("I try to book that seat")
def try_book_seat(context):
    context.response = context.client.get(f"/seats/{context.seat.id}/book/", follow=False)

@then("I should be redirected to the login page")
def redirected_to_login(context):
    assert context.response.status_code in (301, 302)
    assert "/accounts/login/" in context.response["Location"]

@then("the seat should be marked booked")
def seat_marked_booked(context):
    context.seat.refresh_from_db()
    assert context.seat.booking_status is True

@then("a booking should exist for that user and seat")
def booking_exists(context):
    assert Booking.objects.filter(user=context.user, seat=context.seat).exists()