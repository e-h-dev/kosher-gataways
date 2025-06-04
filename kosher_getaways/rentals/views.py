from django.shortcuts import render, get_object_or_404
from .models import Rentals, Image

# Create your views here.


def rentals(request):

    rentals = Rentals.objects.prefetch_related('images').all()

    context = {
        "rentals": rentals,
        }
    return render(request, 'rentals/rentals.html', context)


def rental_detail(request, rental_id):
    rental = get_object_or_404(Rentals.objects.prefetch_related('images').all(), pk=rental_id)
    image = Image.objects.all()

    context = {
        "rental": rental,
        "image": image
        }
    return render(request, 'rentals/rental_detail.html', context)
