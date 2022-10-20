from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
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


class CreateEvent(View):
    """
    Loads page with form for event creation
    """
    def get(self, request):

        return render(request, "create-event.html", {"event_form": EventForm()})

    def post(self, request, slug=None, *args, **kwargs):
        event_form = EventForm(data=request.POST)
        print(event_form)
        queryset = Event.objects.filter(post=1)
        print(queryset)
        event = queryset
        print(event)

        event_form = EventForm(data=request.POST)
        if event_form.is_valid():
            print(event_form)
            event_form.save()
        else:
            event_form = EventForm()

        return HttpResponseRedirect(reverse('events'))

        # return render(
        #     request, "events.html", 
        #     {
        #         "event": event,
        #         "event_form": event_form
        #     }
        # )
