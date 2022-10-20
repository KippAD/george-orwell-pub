from .models import Event
from django import forms


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'date', 'time', 'price', 'capacity', 'post',)
    
    widgets = {
        'title': forms.TextInput(attrs={'class':"form-control", 'placeholder':'Enter Title'}),
        'description': forms.TextInput(attrs={'class':"form-control", 'placeholder':'Enter description'}),
        'date': forms.TimeField(),
        'time': forms.DateField(),
        'price': forms.IntegerField(),
        'capacity': forms.IntegerField(),
        }