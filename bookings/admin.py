from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingPost(SummernoteModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'user',
        'event',
        'booking_count'
        )
    search_fields = ['event', ]
    list_filter = ('event',)
