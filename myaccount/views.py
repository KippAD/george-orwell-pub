from .forms import ContactForm
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from bookings.models import Booking
from events.models import Event
from .models import Message
from django.views import View
from django.shortcuts import render, redirect


class AccountPage(View):
    template_name = 'account.html'
    contact_form = ContactForm

    def get(self, request):
        user = self.request.user
        bookings = Booking.objects.filter(user=user)
        contact = self.contact_form(None)
        return render(request, self.template_name, {'bookings': bookings, 'contact': contact, 'user': user, })

    def post(self, request, *args, **kwargs):
        user = self.request.user
        bookings = Booking.objects.filter(user=user)
        
        contact_form = ContactForm(data=request.POST)
        if request.method == 'POST' and 'send-message' in request.POST:
            if contact_form.is_valid():
                contact_form.instance.msg_sender = self.request.user
                contact_form.save()
            else:
                self.contact_form = ContactForm()

            return render(request, 'account.html', {'bookings': bookings, 'contact': contact_form, 'user': user, })


class AdminPage(View):
    template_name = 'admin.html'

    def get(self, request):
        messages = Message.objects.all()
        events = Event.objects.all()
        bookings = Booking.objects.all()
        User = get_user_model()
        users = User.objects.all()
        return render(
            request, 
            'admin.html',
            {
                'bookings': bookings,
                'events': events,
                'messages': messages,
                'users': users,
                })


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")