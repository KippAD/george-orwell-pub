from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from .models import Booking
from .forms import BookingForm
from django.http import HttpResponseRedirect


class BookEvent(LoginRequiredMixin, generic.CreateView):
    """
    Loads booking form template and ensures that a user can't
    double book and event or book an event that is already
    full
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

        total_bookings = sum(Booking.objects.values_list(
            'booking_count', flat=True))
        booking = int(form.instance.booking_count)
        capacity = int(form.instance.event.capacity)
        # +2 is short fix for capacity error
        free_space = (capacity - total_bookings) + 2

        for b in Booking.objects.all():
            if b.user == user and b.event == event:
                return HttpResponseRedirect(reverse('bookings:exists'))

        if booking <= free_space:
            form.instance.user = user
            return super().form_valid(form)
        elif booking > free_space:
            return HttpResponseRedirect(reverse('bookings:event-full'))


class UpdateBooking(SuccessMessageMixin, generic.UpdateView):
    """
    Updates user's event booking and redirects depending on
    whether user is staff member
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


# Check who is owner of booking or not redirect to 404
class DeleteBooking(SuccessMessageMixin, generic.DeleteView):
    """
    Deletes user's event booking and displays a succes message
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


class BookingExistsError(generic.TemplateView):
    """Displays error page for booking form"""
    template_name = "existing-booking-error.html"


class FullEventError(generic.TemplateView):
    """Displays error page for booking form"""
    template_name = "event-full-error.html"
