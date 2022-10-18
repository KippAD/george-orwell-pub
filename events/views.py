from django.shortcuts import render
from django.views import generic, View
from .models import Event


class HomePage(View):
    """
    Renders the home page index.html
    """
    def get(self, request):
        return render(request, "index.html")


# class EventList(View):
#     """
#     Renders the events schedule list
#     """
#     def get(self, request):
#         return render(request, "events.html")


class EventList(generic.ListView):
    """
    Renders the events schedule list
    """
    model = Event
    queryset = Event.objects.filter(post=1).order_by('date_created')
    template_name = "events.html"
    paginate_by = 6
