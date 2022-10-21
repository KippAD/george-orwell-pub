from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.urls import reverse_lazy
from django.views import generic, View
from .models import Event
from .forms import EventForm


class HomePage(View):
    """
    Renders the home page index.html
    """
    def get(self, request):
        return render(request, "index.html")


class EventList(generic.ListView):
    """
    Renders the events schedule list
    """
    model = Event
    queryset = Event.objects.filter(post=1).order_by('date_created')
    template_name = "events.html"
    paginate_by = 6


class CreateEvent(generic.CreateView):
    """
    Creates event
    """
    model = Event
    template_name = "create-event.html"
    form_class = EventForm
    success_url = "/events/"


class UpdateEvent(generic.UpdateView):
    """
    Updates event
    """
    model = Event
    template_name = "create-event.html"
    form_class = EventForm
    success_url = "/events/"


class DeleteEvent(generic.DeleteView):
    """
    Deletes event
    """
    model = Event
    success_url = reverse_lazy("events")
