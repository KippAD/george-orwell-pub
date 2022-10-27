from django.urls import path
from bookings.views import UpdateBooking, DeleteBooking
from .views import AccountPage, AdminPage, logout_view


app_name = "myaccount"

urlpatterns = [
    path('myaccount', AccountPage.as_view(), name='account'),
    path('admin', AdminPage.as_view(), name="admin"),
    path('update/<int:pk>', UpdateBooking.as_view(), name='update-booking'),
    path('delete/<int:pk>', DeleteBooking.as_view(), name='delete-booking'),
    path('logout', logout_view, name="logout")
]