from django.shortcuts import render
from .models import Rentals, Image

# Create your views here.


# def rentals(request):

#     rentals = Rentals.objects.all()
#     return render(request, 'rentals/rentals.html', {"rentals": rentals})


def rentals(request):

    image = Image.objects.all()
    rentals = Rentals.objects.all()

    # load_image = image.objects.all()

    context = {
        "rentals": rentals,
        "image": image,
        # "load_image": load_image,
        }

    return render(request, 'rentals/rentals.html', context)
