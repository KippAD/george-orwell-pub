from django import forms
from .models import Message


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('msg_subject', 'msg_content',)
        labels = {
            "msg_subject":  "Subject",
            "msg_content": "Message Content",
    }
