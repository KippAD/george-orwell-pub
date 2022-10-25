from django.shortcuts import get_object_or_404, render
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Booking
from .forms import BookingForm, ContactForm


class AccountPage(View):
    template_name = 'account.html'
    contact_form = ContactForm

    def get(self, request):
        user = self.request.user
        bookings = Booking.objects.filter(user=user)
        contact = self.contact_form(None)
        return render(request, self.template_name, {'bookings': bookings, 'contact': contact, 'user': user, })

    def post(self, request, *args, **kwargs):
        user = self.request.user
        bookings = Booking.objects.filter(user=user)
        
        contact_form = ContactForm(data=request.POST)
        if request.method == 'POST' and 'send-message' in request.POST:
            if contact_form.is_valid():
                contact_form.instance.msg_sender = self.request.user
                contact_form.save()
            else:
                self.contact_form = ContactForm()

            return render(request, self.template_name, {'bookings': bookings, 'contact': contact_form, 'user': user, })


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
    success_url = "/events/"
    # Allow repeatable names for different events
    # Only allow one booking per event per account
    # Pre fill event from button clicked on

    # Ensures that total booking is less than capacity of event
    def form_valid(self, form):
        total_bookings = sum(Booking.objects.values_list('booking_count', flat=True))
        booking = form.instance.booking_count
        capacity = form.instance.event.capacity

        if total_bookings <= capacity and booking <= (capacity - total_bookings):
            form.instance.user = self.request.user
            return super().form_valid(form)
        else:
            print("Error")
