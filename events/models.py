from django.db import models
from django.contrib.auth.models import user
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator


# Model for events
class Events(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = CloudinaryField('image', default='placeholder')
    description = models.TextField(blank=True)
    time = models.TimeField()
    date = models.DateTimeField()
    price = models.IntegerField()
    repeating = models.BooleanField(default=False)
    capacity = models.IntegerField(
        validators=[
            MaxValueValidator(64),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return self.title


