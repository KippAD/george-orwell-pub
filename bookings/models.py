from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from events.models import Event


# Model for bookings
class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE,
                            related_name="event")
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                            related_name="user")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    booking_count = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )