from django.urls import path
from events import views
from django.urls import reverse_lazy
from bookings.views import BookEvent

app_name = 'events'
urlpatterns = [
    path('events/', views.EventList.as_view(), name='events'),
    path('create-event/', views.CreateEvent.as_view(), name='create-event'),
    path('book/<slug:slug>', BookEvent.as_view(), name='book-event'),
    path('update/<slug:slug>', views.UpdateEvent.as_view(), name='update-event'),
    path('delete/<slug:slug>', views.DeleteEvent.as_view(), name='delete-event'),
]

