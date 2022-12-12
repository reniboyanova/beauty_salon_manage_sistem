from django.db import models


class AddProducts(models.Model):
    BRANDS = [('L\'Oreal', 'L\'Oreal'), ('Joico', 'Joico'), ('MOROCCANOIL', 'MOROCCANOIL'), ]
    MAX_LEN_TYPE_OF_PRODUCT = 150
    MAX_LEN_SERIAL_NUMBER = 150
    brand = models.CharField(
        max_length=MAX_LEN_TYPE_OF_PRODUCT,
        choices=BRANDS,
        verbose_name='Brand:',
        null=False,
        blank=False,
    )

    type_of_product = models.CharField(
        max_length=MAX_LEN_TYPE_OF_PRODUCT,
        null=False,
        blank=False,
        verbose_name='Product type:',
    )

    serial_number = models.CharField(
        max_length=MAX_LEN_SERIAL_NUMBER,
        null=False,
        blank=False,
        verbose_name='Serial number:',
    )

    grams = models.PositiveIntegerField(
        verbose_name='Volume(grams):'
    )

    image_of_product = models.URLField(
        verbose_name='Product image:'
    )

    @property
    def information_about_product(self):
        return f'{self.brand} - {self.type_of_product} with serial #{self.serial_number}'

    def __str__(self):
        return f'{self.brand} - {self.type_of_product} with serial #{self.serial_number}'

    class Meta:
        verbose_name_plural = 'Product list'


