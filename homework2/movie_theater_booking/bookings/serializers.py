from rest_framework import serializers
from .models import Movie, Seat, Booking, Showing
# ChatGPT told me to make this file and the django documentation mentions a similar idea.
# ChatGPT helped me with this first serializer, but all others were made by me.
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
    
class ShowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showing
        fields = '__all__'

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'