from django.shortcuts import render
from django.urls import reverse
from django.views import generic, View
from .models import Event
from bookings.models import Booking
from .forms import EventForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class HomePage(generic.ListView):
    """
    Renders the home page index.html
    """
    model = Event
    template_name = "index.html"


class EventPage(View):
    """
    Loads the event page template and passes in the event model
    and the booking count from booking model in a new object
    """
    template_name = 'events.html'

    def get(self, request):
        events_obj = Event.objects.all()
        events = []

        for event in events_obj:
            total = Booking.objects.filter(
                event=event).values_list('booking_count', flat=True)
            booking_count = sum(total)

            new_dict = {
                "date": event.date,
                "title": event.title,
                "desc": event.description,
                "price": event.price,
                "time": event.time,
                "capacity": event.capacity,
                "slug": event.slug,
                "count": booking_count,
            }
            events.append(new_dict)

        return render(
            request,
            'events.html',
            {
                'events': events,
                })


class CreateEvent(generic.CreateView):
    """
    Loads event form and creates event
    """
    model = Event
    template_name = "create-event.html"
    form_class = EventForm
    success_message = "Event Created!"

    def get_success_url(self):
        return reverse("events:events")


class UpdateEvent(SuccessMessageMixin, generic.UpdateView):
    """
    Loads update event form and updates event
    """
    model = Event
    template_name = "update-event.html"
    form_class = EventForm
    success_message = "Event Updated!"

    def get_success_url(self):
        return reverse("myaccount:admin")


class DeleteEvent(SuccessMessageMixin, generic.DeleteView):
    """
    Loads event deletion confirmation and deletes event
    """
    model = Event
    template_name = "confirm-event-deletion.html"
    success_message = "Booking Deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteEvent, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("myaccount:admin")
