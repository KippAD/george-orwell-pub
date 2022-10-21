"""orwellpub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from events import views
from bookings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', views.HomePage.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    path('events/', views.EventList.as_view(), name='events'),
    path('events/create-event/', views.CreateEvent.as_view(), name='create-event'),
    path('events/book/<slug:slug>', views.BookEvent.as_view(), name='book-event'),
    path('events/update/<slug:slug>', views.UpdateEvent.as_view(), name='update-event'),
    path('events/delete/<slug:slug>', views.DeleteEvent.as_view(), name='delete-event'),
]
