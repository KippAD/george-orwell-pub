from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    msg_sender = models.ForeignKey(User, related_name="msg_sender",
                                   on_delete=models.CASCADE)
    msg_subject = models.CharField(max_length=100, blank=False)
    msg_content = models.TextField(blank=True)
    time_sent = models.DateTimeField(auto_now_add=True)

