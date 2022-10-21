from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.template.defaultfilters import slugify

POST = ((0, "Draft"), (1, "Post"))


# Model for events
class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
