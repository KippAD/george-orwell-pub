from django.urls import path
from events.views import EventPage, CreateEvent, UpdateEvent, DeleteEvent

app_name = 'events'
urlpatterns = [
    path('events/', EventPage.as_view(), name='events'),
    path('create-event/', CreateEvent.as_view(), name='create-event'),
    path('update/<slug:slug>', UpdateEvent.as_view(), name='update-event'),
    path('delete/<slug:slug>', DeleteEvent.as_view(), name='delete-event'),
]
