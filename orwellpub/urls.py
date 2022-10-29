from django.contrib import admin
from django.urls import path, include
from events import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', views.HomePage.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    path('events/', include('events.urls', namespace='events')),
    path('myaccount/', include('myaccount.urls', namespace='myaccount')),
    path('bookings/', include('bookings.urls', namespace='bookings')),
]
