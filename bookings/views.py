from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from .models import Booking
from .forms import BookingForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


class BookEvent(LoginRequiredMixin, generic.CreateView):
    """
    Books event for user
    """
    model = Booking
    template_name = "book-event.html"
    form_class = BookingForm

    def get_success_url(self):
        return reverse("bookings:booking-successful")

    # Ensures that total booking is less than capacity of event
    def form_valid(self, form):
        user = self.request.user
        event = form.instance.event

        total_bookings = sum(Booking.objects.values_list('booking_count', flat=True))
        booking = form.instance.booking_count
        capacity = form.instance.event.capacity

        if booking > (capacity - total_bookings):
            return HttpResponseRedirect(reverse('bookings:event-full')) 

        for b in Booking.objects.all():
            if b.user == user and b.event == event:
                return HttpResponseRedirect(reverse('bookings:existing-booking'))
            else:
                form.instance.user = user
                return super().form_valid(form)


class UpdateBooking(SuccessMessageMixin, generic.UpdateView):
    """
    Updates event
    """
    model = Booking
    template_name = "update-booking.html"
    form_class = BookingForm
    success_message = "Booking Updated!"

    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse("myaccount:admin")
        else:
            return reverse("myaccount:account")


class DeleteBooking(SuccessMessageMixin, generic.DeleteView):
    """
    Deletes booking
    """
    model = Booking
    success_message = "Booking Deleted!"
    template_name = 'confirm-booking-deletion.html'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteBooking, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse("myaccount:admin")
        else:
            return reverse("myaccount:account")



class BookingSuccessful(generic.TemplateView):
    """Displays success page for booking form"""
    template_name = "successful-booking.html"


class ExistingBookingError(generic.TemplateView):
    """Displays error page for booking form"""
    template_name = "existing-booking-error.html"


class FullEventError(generic.TemplateView):
    """Displays error page for booking form"""
    template_name = "event-full-error.html"
