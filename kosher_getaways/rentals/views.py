from django.shortcuts import render
from .models import Rentals, Image

# Create your views here.


def rentals(request):

    rentals = Rentals.objects.all()

    # rental_name = Rentals.objects.values_list('name')
    rental_id = Rentals.objects.values_list('id')

    image = Image.objects.all()

    image_name = Image.objects.values_list('name')

    print(image_name)

    # for r_id in rental_id:
    #     print(r_id)
    # print('-------------------')
    # print('-                 -')
    # print('-                 -')
    # print('-                 -')
    # print('-                 -')
    # print('-                 -')
    # print('-------------------')
    # for i_nm in image_name:
    #     print(i_nm)

    # if r_id is i_nm:
    #     print('match')
    # else:
    #     print('not a fit')

    # length = rentals.count()

    # # print(rental_id)
    # # print(image_name)
    # print(image)
    # print('-------------------')
    # print('-                 -')
    # print('-                 -')
    # print('-                 -')
    # print('-                 -')
    # print('-                 -')
    # print('-------------------')
    # print(rentals)
    # print(length)
    context = {
        "rentals": rentals,
        "image": image,
        'image_name': image_name,
        'rental_id': rental_id,
        # 'r_id': r_id,
        # 'i_nm': i_nm,
        }
    return render(request, 'rentals/rentals.html', context)


# def rental_image(request, rentals_id):

#     rentals = Rentals.objects.all()
#     load_image = Image.objects.all()

#     image = get_list_or_404(request, pk=rentals_id)

#     context = {
#         "rentals": rentals,
#         "image": image,
#         "load_image": load_image,
#         }

#     return render(request, 'rentals/rentals.html', context)
