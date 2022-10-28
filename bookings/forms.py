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

    def clean(self):
        clean_booking = super().clean()
        first_name = clean_booking.get('first_name')
        last_name = clean_booking.get('last_name')

        for c in first_name:
            if c.isdigit():
                raise forms.ValidationError({'first_name': 'Your first name cannot include numbers!'})
            elif (' ' in c):
                raise forms.ValidationError({'first_name': 'Your first name cannot include spaces!'})
            elif not c.isalnum():
                raise forms.ValidationError({'first_name': 'Your first name cannot include special characters!'})

        for c in last_name:
            if c.isdigit():
                raise forms.ValidationError({'last_name': 'Your first name cannot include numbers!'})
            elif (' ' in c):
                raise forms.ValidationError({'last_name': 'Your first name cannot include spaces!'})
            elif not c.isalnum():
                raise forms.ValidationError({'last_name': 'Your last name cannot include special characters!'})

        return clean_booking

