from django.urls import path
from bookings.views import BookingExistsError, FullEventError, BookEvent, \
    BookingSuccessful, UpdateBooking, DeleteBooking

app_name = 'bookings'

urlpatterns = [
    path('book', BookEvent.as_view(), name='book-event'),
    path('update/<int:pk>', UpdateBooking.as_view(), name='update-booking'),
    path('delete/<int:pk>', DeleteBooking.as_view(), name='delete-booking'),
    path('error/exists', BookingExistsError.as_view(), name='booking-exists'),
    path('error/full', FullEventError.as_view(), name='event-full'),
    path('success', BookingSuccessful.as_view(), name='booking-successful'),
]
