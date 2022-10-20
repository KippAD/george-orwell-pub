from django.contrib import admin
from django.urls import path, include
from events import views

urlpatterns = [
    path('events/', views.EventList.as_view(), name='events'),
    path('events/create-event/', views.CreateEvent.as_view(), name='create-event'),
]
