from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Booking
from .forms import BookingForm
from events.views import HomePage, EventList, CreateEvent, UpdateEvent, DeleteEvent


class BookEvent(LoginRequiredMixin, generic.CreateView):
    """
    Books event for user
    """
    model = Booking
    template_name = "book-event.html"
    form_class = BookingForm
    success_url = "/events/"
    # Fix total count exceeding capacity
    # Allow repeatable names for different events
    # Only allow one booking per event per account
    def form_valid(self, form):

        total_count = 0
        bookings = Booking.objects.values_list('booking_count', flat=True)
        capacity = form.instance.event.capacity
       
        for booking in bookings:
            total_count += booking
            
            if total_count <= capacity:
                form.instance.user = self.request.user
                return super().form_valid(form)
            else:
                print("Error")
