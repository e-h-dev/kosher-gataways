from django.db import models

# Create your models here.


class Location(models.Model):

    name = models.CharField(max_length=52)

    def __str__(self):
        return self.name
    

class Rentals(models.Model):

    class Meta:
        verbose_name_plural = "Rentals"

    location = models.ForeignKey('Location', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    mini_description = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # image = models.ImageField(null=True, blank=True)
    available_from = models.DateField()
    available_till = models.DateField()
    rating = models.IntegerField(default=1,
                                 choices=((i, i) for i in range(1, 6)))
    review = models.TextField(max_length=600, null=True, blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.ForeignKey('Rentals', null=True, blank=True,
                             on_delete=models.SET_NULL)
    image = models.ImageField(null=True, blank=True)
