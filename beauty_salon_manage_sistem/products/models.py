from django.db import models


class AddProducts(models.Model):
    BRANDS = [('L\'Oreal', 'L\'Oreal'), ('Joico', 'Joico'), ('MOROCCANOIL', 'MOROCCANOIL'), ]
    MAX_LEN_TYPE_OF_PRODUCT = 150
    MAX_LEN_SERIAL_NUMBER = 150
    type_of_product = models.CharField(
        max_length=MAX_LEN_TYPE_OF_PRODUCT,
        null=False,
        blank=False,
    )

    serial_number = models.CharField(
        max_length=MAX_LEN_SERIAL_NUMBER,
        null=False,
        blank=False,
    )

    grams = models.PositiveIntegerField(
    )

    image_of_product = models.URLField()

