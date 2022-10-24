from .models import Booking
from myaccount.models import Message
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('event', 'first_name', 'last_name', 'booking_count',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('msg_subject', 'msg_content',)

