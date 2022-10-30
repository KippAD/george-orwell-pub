from django.test import TestCase
from .forms import ContactForm

class TestContactForm(TestCase):
    
    def test_first_name_is_required(self):
        form = ContactForm(date={'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
    
    def test_last_name_is_required(self):
        form = ContactForm(date={'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
   
    def test_email_is_required(self):
        form = ContactForm(date={'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())