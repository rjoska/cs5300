from django.urls import path
from . import views
# Following the Django tutorial https://docs.djangoproject.com/en/6.0/intro/tutorial01/
#ChatGPT helped me make the movies/id/seats line as I was unsure how to reference an id from the database
# Remember to ask if it should have an admin page
urlpatterns = [
    path('', views.home, name='home'),
    path('movies-page/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_id>/showings/', views.showing_list, name='showing_list'), #changed to make it so it takes a movie id
    path('showings/<int:showing_id>/seats/', views.seat_list, name='seat_list'),
    path('bookings-page/', views.booking_history, name='booking_history'),
    path('signup/', views.signup, name='signup'),
    path('seats/<int:seat_id>/book/', views.book_seat, name='book_seat'), #ChatGPT gave me the idea to add a seperate booking seat page
]