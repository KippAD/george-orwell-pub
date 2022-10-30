from .models import Event
from django import forms
import datetime


# Form for event creation
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
            'title',
            'description',
            'date',
            'time',
            'price',
            'capacity',
            'post',
            )

        widgets = {
            'title': forms.widgets.TextInput(
                attrs={'placeholder': 'Enter the event title'}),
            'description': forms.widgets.Textarea(
                attrs={'rows': 5, 'placeholder': 'Enter a description...'}),
            'date': forms.widgets.DateInput(
                attrs={'type': 'date'}),
            'time': forms.widgets.TimeInput(
                attrs={'type': 'time'}),
            'price': forms.widgets.NumberInput(
                attrs={'placeholder': 'Enter the price of entry'}),
            'capacity': forms.widgets.NumberInput(
                attrs={'placeholder': 'Enter the event capacity (Max: 64)'}),
            'post': forms.widgets.Select(
                attrs={'class': 'form-select' ' form-select-lg' ' fs-5'}),
            }

    # Prevents event date from being set to a past date
    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError(
                "The event date cannot be in the past!"
                )
        return date

    # Prevents numbers from being included in event title
    def clean_title(self):
        title = self.cleaned_data['title']
        for c in title:
            if c.isdigit():
                raise forms.ValidationError("No numbers!")
        return title
