from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('event', 'first_name', 'last_name', 'booking_count',)

