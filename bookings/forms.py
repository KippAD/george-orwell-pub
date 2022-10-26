from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('event', 'first_name', 'last_name', 'booking_count',)

        widgets = {
            'event': forms.widgets.Select(attrs={'class': 'form-select' ' form-select-lg' ' fs-5'}),
            'first_name': forms.widgets.TextInput(attrs={'placeholder': 'Enter your first name'}),
            'last_name': forms.widgets.TextInput(attrs={'placeholder': 'Enter your last name'}),
            'booking_count': forms.widgets.NumberInput(attrs={'placeholder': 'How many people are you booking for? (Max: 5)'}),
            }

