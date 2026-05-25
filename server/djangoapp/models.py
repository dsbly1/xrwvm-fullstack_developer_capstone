from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30)
    description = models.CharField(null=False, max_length=200)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(
        CarMake, null=True, on_delete=models.CASCADE)
    dealer_id = models.IntegerField(null=True)
    name = models.CharField(null=False, max_length=30)

    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "Wagon"
    TYPE_CHOICES = [
        (SEDAN, "Sedan"),
        (SUV, "SUV"),
        (WAGON, "Wagon"),
    ]
    type = models.CharField(
        null=False,
        max_length=10,
        choices=TYPE_CHOICES,
        default=SEDAN
    )
    year = models.IntegerField(
        null=False,
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )

    def __str__(self):
        return self.name + " " + self.car_make.name
