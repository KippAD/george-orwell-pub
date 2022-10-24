from .forms import ContactForm
from bookings.views import Booking
from django.views import generic, render
from django.contrib.auth.mixins import LoginRequiredMixin


# def ContactForm(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             pass
#     else:
#         form = ContactForm()
#     return render(request, 'account.html', {'form': form})
