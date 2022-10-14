from django.shortcuts import render
from django.views import View
from .models import Event


class HomePage(View):
    """
    Renders the home page index.html
    """
    def get(self, request):
        return render(request, "index.html")
