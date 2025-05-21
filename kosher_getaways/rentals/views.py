from django.shortcuts import render
from .models import Rentals

# Create your views here.


def rentals(request):

    rentals = Rentals.objects.all()
    return render(request, 'rentals/rentals.html', {"rentals": rentals})
