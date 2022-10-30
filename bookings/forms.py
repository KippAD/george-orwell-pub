from .models import Booking
from django import forms


# User form to make a booking for an event
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('event', 'first_name', 'last_name', 'booking_count',)

        widgets = {
            'event': forms.widgets.Select(
                attrs={'class': 'form-select' ' form-select-lg' ' fs-5'}),
            'first_name': forms.widgets.TextInput(
                attrs={'placeholder': 'Enter your first name'}),
            'last_name': forms.widgets.TextInput(
                attrs={'placeholder': 'Enter your last name'}),
            'booking_count': forms.widgets.NumberInput(attrs={
                'placeholder': 'Number of reservations (Max: 5)'}),
            }

    # Form validation
    def clean(self):
        clean_booking = super().clean()
        first_name = clean_booking.get('first_name')
        last_name = clean_booking.get('last_name')
        # Prevents numbers, spaces, and special characters
        for c in first_name:
            if c.isdigit():
                raise forms.ValidationError(
                    {'first_name': 'Cannot include numbers!'}
                    )
            elif (' ' in c):
                raise forms.ValidationError(
                    {'first_name': 'Cannot include spaces!'}
                    )
            elif not c.isalnum():
                if c == "-":
                    pass
                else:
                    raise forms.ValidationError(
                        {'first_name': 'Cannot include special characters!'}
                        )
        # Prevents numbers, spaces, and special characters
        for c in last_name:
            if c.isdigit():
                raise forms.ValidationError(
                    {'last_name': 'Cannot include numbers!'}
                    )
            elif (' ' in c):
                raise forms.ValidationError(
                    {'last_name': 'Cannot include spaces!'}
                    )
            elif not c.isalnum():
                if c == "-":
                    pass
                else:
                    raise forms.ValidationError(
                        {'last_name': 'Cannot include special characters!'}
                        )
        return clean_booking
