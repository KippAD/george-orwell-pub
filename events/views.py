from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic, View
from .models import Event
from bookings.models import Booking
from .forms import EventForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class HomePage(generic.ListView):
    """
    Renders the home page index.html
    """
    model = Event
    template_name = "index.html"


class EventPage(View):
    template_name = 'events.html'

    def get(self, request):
        events_obj = Event.objects.all()
        events = []

        for event in events_obj:
            booking_count = sum(Booking.objects.filter(event=event).values_list('booking_count', flat=True))

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
    Creates event
    """
    model = Event
    template_name = "create-event.html"
    form_class = EventForm
    success_message = "Event Created!"

    def get_success_url(self):
        return reverse("events:events")


class UpdateEvent(SuccessMessageMixin, generic.UpdateView):
    """
    Updates event
    """
    model = Event
    template_name = "update-event.html"
    form_class = EventForm
    success_message = "Event Updated!"

    def get_success_url(self):
        return reverse("events:events")


class DeleteEvent(SuccessMessageMixin, generic.DeleteView):
    """
    Deletes event
    """
    model = Event
    success_message = "Booking Deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteEvent, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("events:events")


