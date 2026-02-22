from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie, Seat, Booking, Showing
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer, ShowingSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from collections import defaultdict
import re


# Create your views here.
#ChatGPT helped me make the first view set.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ShowingViewSet(viewsets.ModelViewSet):
    queryset = Showing.objects.all()
    serializer_class = ShowingSerializer

# Due to the changes made for seating where we need to only show seats for the specific movie showing
# It seems its recomended to show all if we fail to find a specific showing. 
class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    # ChatGPT helped me make this becasue I knew I wanted to only show specifics but the documents didn't help the most
    def get_queryset(self):
        showing_id = self.request.query_params.get('showing')
        if showing_id:
            return Seat.objects.filter(showing_id=showing_id)
        return Seat.objects.all()

# I need to autheticate the user so I found an authenticate function in rest. ChatGPT gave me an example and mine is based on that
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user) #check if the use is the same as the self.user
    # ChatGPT made this as I would not have thought that I would need to update the booking here
    def perform_create(self, serializer):
        booking = serializer.save(user=self.request.user)
        seat = booking.seat
        seat.booking_status = True
        seat.save()

# ChatGPT also suggested making these for later. (It made the movie_list and home, I did the others)
def home(request):
    return render(request, 'bookings/home.html')

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

#ChatGPT made this. I am learning a lot about render, but man am I struggling to find the resources.
def showing_list(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    showings = Showing.objects.filter(movie_id=movie_id)

    return render(
        request,
        'bookings/showing_list.html',
        {
            'movie': movie,
            'showings': showings
        }
    )

# I made this one following the example chatGPT made me above. Man any change I want on the page must be made here
def seat_list(request, showing_id):
    showing = get_object_or_404(Showing, id=showing_id)
    seats = Seat.objects.filter(showing_id=showing_id)

    return render(
        request,
        'bookings/seat_booking.html',
        {
            'seats': seats,
            'showing': showing
        }
    )


@login_required
def booking_history(request):
    #ChatGPT helped me with the object filter as I wanted to ensure that you only saw your user requests.
    bookings = Booking.objects.filter(user=request.user).select_related(
        'seat__showing__movie',
        'seat__showing',
        'seat'
    )
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})

# ChatGPT made this as user sign in stuff has always been a weak point for me in any language
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # goes to /accounts/login/
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

#ChatGPT made this for me as well as again user auth is a weak point
@login_required
def book_seat(request, seat_id):
    seat = get_object_or_404(Seat, id=seat_id)

    # prevent double booking
    if seat.booking_status:
        return render(request, 'bookings/seat_already_booked.html', {'seat': seat})

    # create booking + mark seat booked
    Booking.objects.create(seat=seat, user=request.user, booking_date=timezone.now())
    seat.booking_status = True
    seat.save()

    return redirect('booking_history')

# This is to help with rendering all the seats ChatGPT helped me make this. I made some parts but the final product was all managed by ChatGPT
def seat_list(request, showing_id):
    seats = Seat.objects.filter(showing_id=showing_id)

    # ChatGPT made this as regular expressions are something I have never worked with in python
    def parse_seat(seat_num: str):
        match = re.match(r"^([A-Za-z]+)(\d+)$", seat_num.strip())
        if not match:
            # fallback for weird seat labels
            return (seat_num, 0)
        row = match.group(1).upper()
        num = int(match.group(2))
        return (row, num)

    seat_rows = defaultdict(list)

    for seat in seats:
        row, num = parse_seat(seat.seat_number)
        seat_rows[row].append((num, seat))
    
    ordered_rows = []
    for row in sorted(seat_rows.keys()):
        ordered_seats = [seat for (num, seat) in sorted(seat_rows[row], key=lambda x: x[0])]
        ordered_rows.append((row, ordered_seats))

    return render(request, "bookings/seat_booking.html", {"seat_rows": ordered_rows})