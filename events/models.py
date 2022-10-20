from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator

POST = ((0, "Draft"), (1, "Post"))


# Model for events
class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField()
    price = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    repeating = models.BooleanField(default=False)
    post = models.IntegerField(choices=POST, default=0)
    capacity = models.IntegerField(
        validators=[
            MaxValueValidator(64),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return self.title


