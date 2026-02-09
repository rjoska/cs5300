from django.db import models

# Create your models here.
class Movie(models.Model):
    title = model.CharField(max_length=180)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField(help_text="Time in minutes")

class Seat(models.Model):
    seat_number = models.CharField(max_length=3)
    booking_status = models.BooleanField()

class Booking(models.Model):
    