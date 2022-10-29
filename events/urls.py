from django.urls import path
from events import views
from bookings.views import BookEvent
from django.urls import reverse_lazy

app_name = 'events'
urlpatterns = [
    path('events/', views.EventPage.as_view(), name='events'),
    path('create-event/', views.CreateEvent.as_view(), name='create-event'),
    path('update/<slug:slug>', views.UpdateEvent.as_view(), name='update-event'),
    path('delete/<slug:slug>', views.DeleteEvent.as_view(), name='delete-event'),
]
