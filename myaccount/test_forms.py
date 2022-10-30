from django.test import TestCase
from .forms import ContactForm


# Tests the validation of user contact form
class TestContactForm(TestCase):
    # Tests that first name field cannot be empty input
    def test_first_name_is_required(self):
        form = ContactForm(date={'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
    
    # Tests that last name field cannot be empty input
    def test_last_name_is_required(self):
        form = ContactForm(date={'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
    
    # Tests that email field cannot be empty input
    def test_email_is_required(self):
        form = ContactForm(date={'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
