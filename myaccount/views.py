from .forms import ContactForm
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from bookings.models import Booking
from events.models import Event
from django.views import View
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


class AccountPage(View):
    template_name = 'account.html'
    contact_form = ContactForm

    def get(self, request):
        user = self.request.user
        bookings = Booking.objects.filter(user=user)
        contact = self.contact_form(None)
        return render(request, self.template_name, {'bookings': bookings, 'contact': contact, 'user': user, })


class AdminPage(View):
    template_name = 'admin.html'

    def get(self, request):
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
                'users': users,
                })


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry" 
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'georgeorwellpub@outlook.com', ['georgeorwellpub@outlook.com'])
                return render(request, "contact-success.html") 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

    form = ContactForm()
    return render(request, "contact.html", {'form':form})

