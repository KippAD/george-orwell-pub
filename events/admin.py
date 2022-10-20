from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventPost(SummernoteModelAdmin):
    list_display = ('title', 'date', 'price', 'date_created')
    search_fields = ['title', 'description']
    list_filter = ('price', 'date_created')
    prepopulated_fields = {'slug': ('title',)}
