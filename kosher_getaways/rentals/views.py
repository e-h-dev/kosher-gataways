from django.shortcuts import render, get_object_or_404
from .models import Rentals, Image

# Create your views here.


def rentals(request):

    rentals = Rentals.objects.all()

    # rentals = Rentals.objects.all().prefetch_related('image_set')

    # rental_name = Rentals.objects.values_list('name')
    rental_id = Rentals.objects.values_list('id')

    image = Image.objects.all()

    # image = Image.objects.all().select_related(Rentals)

    image_name = Image.objects.values_list('name')

    
    # for r in rental_id:
    #     rent = r
    #     print(rent)

    context = {
        "rentals": rentals,
        "image": image,
        'image_name': image_name,
        'rental_id': rental_id,
        }
    return render(request, 'rentals/rentals.html', context)


def rental_detail(request, rental_id):
    rental = get_object_or_404(Rentals, pk=rental_id)
    image = Image.objects.all()

    context = {
        "rental": rental,
        "image": image
        }
    return render(request, 'rentals/rental_detail.html', context)

