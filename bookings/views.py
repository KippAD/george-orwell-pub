from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from .models import Booking
from .forms import BookingForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings


class UpdateBooking(generic.UpdateView):
    """
    Updates event
    """
    model = Booking
    template_name = "book-event.html"
    form_class = BookingForm
    success_url = "/accounts/myaccount/"


class DeleteBooking(generic.DeleteView):
    """
    Deletes booking
    """
    model = Booking
    success_url = reverse_lazy("account")


class BookEvent(LoginRequiredMixin, generic.CreateView):
    """
    Books event for user
    """
    model = Booking
    template_name = "book-event.html"
    form_class = BookingForm

    def get_success_url(self):
        return reverse("events:events")

    # Ensures that total booking is less than capacity of event
    def form_valid(self, form):
        user = self.request.user
        event = form.instance.event

        total_bookings = sum(Booking.objects.values_list('booking_count', flat=True))
        booking = form.instance.booking_count
        capacity = form.instance.event.capacity

        if total_bookings <= capacity and booking <= (capacity - total_bookings):
            for b in Booking.objects.all():
                if b.user == user and b.event == event:
                    return HttpResponseRedirect(reverse('events:existing-booking'))

            form.send_mail(
                subject="Test Subject",
                message="Test Email",
                from_email=[settings.EMAIL_HOST_USER],
                recipient_list=['kippad@hotmail.co.uk'],
            )

            form.instance.user = user
            return super().form_valid(form)

        elif total_bookings <= capacity and booking <= (capacity - total_bookings):
            return HttpResponseRedirect(reverse('events:event-full'))


class BookingSuccessful(generic.TemplateView):
    """Displays success page for booking form"""
    template_name = "booking-successful.html"


class ExistingBookingError(generic.TemplateView):
    """Displays error page for booking form"""
    template_name = "existing-booking-error.html"


class FullEventError(generic.TemplateView):
    """Displays error page for booking form"""
    template_name = "event-full-error.html"
