from django.urls import path
from bookings.views import ExistingBookingError, FullEventError, BookEvent, BookingSuccessful, UpdateBooking, DeleteBooking

app_name = 'bookings'

urlpatterns = [
    path('book', BookEvent.as_view(), name='book-event'),
    path('update/<int:pk>', UpdateBooking.as_view(), name='update-booking'),
    path('delete/<int:pk>', DeleteBooking.as_view(), name='delete-booking'),
    path('error/existing-booking', ExistingBookingError.as_view(), name='existing-booking'),
    path('error/event-full', FullEventError.as_view(), name='event-full'),
    path('booking-successful', BookingSuccessful.as_view(), name='booking-successful'),
]
