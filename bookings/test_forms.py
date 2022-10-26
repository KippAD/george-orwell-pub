from django.test import TestCase
from .forms import BookingForm


class TestBookingForm(TestCase):
    """ Tests events app model """

    def test_first_name_is_required(self):
        form = BookingForm({
            'event': "New 1",
            'user': 'admin',
            'first_name': '',
            'last_name': 'Smith',
            'booking_count': 2,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())

    def test_last_name_is_required(self):
        form = BookingForm({
            'event': "New 1",
            'user': 'admin',
            'first_name': 'Tom',
            'last_name': '',
            'booking_count': 2,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())

    def test_booking_count_is_required(self):
        form = BookingForm({
            'event': "New 1",
            'user': 'admin',
            'first_name': 'Tom',
            'last_name': 'Smith',
            'booking_count': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('booking_count', form.errors.keys())

    def test_booking_count_of_0_is_invalid(self):
        form = BookingForm({
            'event': "New 1",
            'user': 'admin',
            'first_name': 'Tom',
            'last_name': 'Smith',
            'booking_count': 0,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('booking_count', form.errors.keys())
 
