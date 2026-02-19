from django.urls import path
from . import views
# I was told to make this file by ChatGPT to help with making URLS that are descriptive
#ChatGPT helped me make this first two example lines, but the others were made by me
urlpatterns = [
    path('', views.home, name='home'),
    path('movies-page/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_id>/showings/', views.showing_list, name='showing_list'), #changed to make it so it takes a movie id
    path('showings/<int:showing_id>/seats/', views.seat_list, name='seat_list'),
    path('bookings-page/', views.booking_history, name='booking_history'),
    path('signup/', views.signup, name='signup'),
    path('seats/<int:seat_id>/book/', views.book_seat, name='book_seat'), #ChatGPT gave me the idea to add a seperate booking seat page
]