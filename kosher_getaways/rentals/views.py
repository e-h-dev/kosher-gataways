from django.shortcuts import render, get_object_or_404
from .models import Rentals, Image

# Create your views here.


def rentals(request):

    rentals = Rentals.objects.all()

    # rental_name = Rentals.objects.values_list('name')
    rental_id = Rentals.objects.values_list('id')

    image = Image.objects.all()

    image_name = Image.objects.values_list('name')
    for i in image_name[0]:
        print(i)

    for r in rental_id:
        print(f'this is what r looks like - {r}')

    # x = (r[0])

    # print(f'this is ythe complete unpack - {image_name[x]}')
    # print(f'this is unpacked rental id - {rental_id[x]}')

    image_id = image_name[0][0]
    rental_unpacked_id = rental_id[0][0]

    if rental_unpacked_id == image_id:
        image = image
    else:
        image = None

    # print(f'this is the result of rental_unpacked_id{rental_unpacked_id}')
    # print(f'this is the result of image_id{image_id}')


    if rental_unpacked_id is image_id:
        print('match')
    else:
        print('no match')
    print(type(rental_unpacked_id))
    print(type(image_id))

    context = {
        "rentals": rentals,
        "image": image,
        'image_name': image_name,
        'rental_id': rental_id,
        # 'my_image': my_image,
        }
    return render(request, 'rentals/rentals.html', context)


def rental_detail(request, rental_id):
    rental = get_object_or_404(Rentals, pk=rental_id)

    context = {
        "rental": rental,
        }
    return render(request, 'rentals/rental_detail.html', context)

