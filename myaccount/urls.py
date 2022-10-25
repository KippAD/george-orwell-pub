from django.urls import path
from bookings import views

app_name = "myaccount"

urlpatterns = [
    path('myaccount', views.AccountPage.as_view(), name='account'),
    path('update/<int:pk>', views.UpdateBooking.as_view(), name='update-booking'),
    path('delete/<int:pk>', views.DeleteBooking.as_view(), name='delete-booking'),
    path('contact/', views.DeleteBooking.as_view(), name='contact-form'),
]