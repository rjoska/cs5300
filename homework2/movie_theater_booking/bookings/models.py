from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Note I used ChatGPT to help me make these models. It gave me an example for the Movie model which is shown here.
class Movie(models.Model):
    title = models.CharField(max_length=190)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField(help_text="Time in minutes")

    def __str__(self):
        return self.title

class Showing(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    start_time = models.DateTimeField()

    def __str__(self):
        return f"{self.movie.title} - {self.start_time}"

#The seat model was adjusted after the TA AI and you offered your suggestions and feedback
class Seat(models.Model):
    showing = models.ForeignKey(Showing, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=5)
    booking_status = models.BooleanField()

    def __str__(self):
        return f"{self.seat_number} - {self.showing}"

#The Booking Model was made by me fully, but ChatGPT as well as the docs helped me make sure the FKey structure was correct.
class Booking(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.seat}"