from django.urls import path
from events import views
from django.urls import reverse_lazy
from bookings.views import ExistingBookingError, FullEventError, BookEvent, BookingSuccessful

app_name = 'events'
urlpatterns = [
    path('events/', views.EventList.as_view(), name='events'),
    path('create-event/', views.CreateEvent.as_view(), name='create-event'),
    path('book/<slug:slug>', BookEvent.as_view(), name='book-event'),
    path('error/existing-booking', ExistingBookingError.as_view(), name='existing-booking'),
    path('error/event-full', FullEventError.as_view(), name='event-full'),
    path('booking-successful', BookingSuccessful.as_view(), name='booking-successful'),
    path('update/<slug:slug>', views.UpdateEvent.as_view(), name='update-event'),
    path('delete/<slug:slug>', views.DeleteEvent.as_view(), name='delete-event'),
]

