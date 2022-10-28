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


class EventList(generic.ListView):
    """
    Renders the events schedule list
    """
    model = Event
    template_name = "events.html"
    paginate_by = 6


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
    template_name = "edit-event.html"
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


