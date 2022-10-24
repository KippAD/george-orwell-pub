from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Message


@admin.register(Message)
class ContactMessage(SummernoteModelAdmin):
    list_display = ('msg_sender', 'time_sent', 'msg_subject',)
    search_fields = ['msg_sender', 'msg_subject', ]
    list_filter = ('msg_sender', 'time_sent', )
